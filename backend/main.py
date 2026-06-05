from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from fastapi.staticfiles import StaticFiles
from fastapi.responses import FileResponse
from pydantic import BaseModel
from typing import Optional, Any
import anthropic
import os
import json
import httpx
from pathlib import Path

app = FastAPI(title="Social AI API")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

client = anthropic.Anthropic(api_key=os.environ.get("ANTHROPIC_API_KEY"))

BASE_DIR = Path(__file__).parent.parent
FRONTEND_DIR = BASE_DIR / "frontend"

app.mount("/static", StaticFiles(directory=str(FRONTEND_DIR)), name="static")

@app.get("/")
def root():
    return FileResponse(str(FRONTEND_DIR / "index.html"))


# ── SUPABASE CONFIG ──────────────────────────────────────────
SUPABASE_URL = os.environ.get("SUPABASE_URL", "https://gbjlacbtiisvzdtlsipw.supabase.co")
SUPABASE_KEY = os.environ.get("SUPABASE_KEY", "")

def supa_headers():
    return {
        "apikey": SUPABASE_KEY,
        "Authorization": f"Bearer {SUPABASE_KEY}",
        "Content-Type": "application/json",
        "Prefer": "return=representation"
    }

def init_db():
    """Tworzy tabelę store przez Supabase REST API."""
    # Supabase REST nie pozwala na CREATE TABLE – tabela musi być stworzona w SQL Editor
    # Sprawdzamy tylko czy połączenie działa
    try:
        r = httpx.get(
            f"{SUPABASE_URL}/rest/v1/store?limit=1",
            headers=supa_headers(),
            timeout=5
        )
        if r.status_code == 404 or (r.status_code == 400 and "does not exist" in r.text):
            print("DB: tabela 'store' nie istnieje – stwórz ją w Supabase SQL Editor")
        else:
            print(f"DB: połączenie OK (status {r.status_code})")
    except Exception as e:
        print(f"DB init warning: {e}")

init_db()


# ── MODELE ──────────────────────────────────────────────────
class GenerateRequest(BaseModel):
    prompt: str
    max_tokens: int = 1200
    image_base64: Optional[str] = None
    image_media_type: Optional[str] = "image/jpeg"

class GenerateResponse(BaseModel):
    content: str
    usage: Optional[dict] = None

class StoreSetRequest(BaseModel):
    key: str
    value: Any

class StoreGetResponse(BaseModel):
    key: str
    value: Any


# ── ENDPOINTY – KV STORE ─────────────────────────────────────
@app.get("/api/store/{key}", response_model=StoreGetResponse)
def store_get(key: str):
    try:
        r = httpx.get(
            f"{SUPABASE_URL}/rest/v1/store?key=eq.{key}&select=value",
            headers=supa_headers(),
            timeout=5
        )
        if r.status_code != 200:
            return StoreGetResponse(key=key, value=None)
        rows = r.json()
        if not rows:
            return StoreGetResponse(key=key, value=None)
        return StoreGetResponse(key=key, value=rows[0]["value"])
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@app.post("/api/store")
def store_set(req: StoreSetRequest):
    try:
        payload = {"key": req.key, "value": req.value}
        r = httpx.post(
            f"{SUPABASE_URL}/rest/v1/store",
            headers={**supa_headers(), "Prefer": "resolution=merge-duplicates,return=minimal"},
            json=payload,
            timeout=5
        )
        if r.status_code not in (200, 201, 204):
            raise HTTPException(status_code=500, detail=r.text)
        return {"ok": True}
    except HTTPException:
        raise
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


# ── ENDPOINTY – AI ───────────────────────────────────────────
@app.post("/api/generate", response_model=GenerateResponse)
def generate(req: GenerateRequest):
    try:
        # Build message content – with or without image
        if req.image_base64:
            messages = [{
                "role": "user",
                "content": [
                    {
                        "type": "image",
                        "source": {
                            "type": "base64",
                            "media_type": req.image_media_type or "image/jpeg",
                            "data": req.image_base64
                        }
                    },
                    {"type": "text", "text": req.prompt}
                ]
            }]
        else:
            messages = [{"role": "user", "content": req.prompt}]

        response = client.messages.create(
            model="claude-sonnet-4-20250514",
            max_tokens=req.max_tokens,
            messages=messages
        )
        content = "".join(
            block.text for block in response.content if hasattr(block, "text")
        )
        return GenerateResponse(
            content=content,
            usage={
                "input": response.usage.input_tokens,
                "output": response.usage.output_tokens
            }
        )
    except anthropic.AuthenticationError:
        raise HTTPException(status_code=401, detail="Nieprawidłowy klucz API.")
    except anthropic.RateLimitError:
        raise HTTPException(status_code=429, detail="Przekroczono limit zapytań.")
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


@app.post("/api/stream")
def stream_endpoint(req: GenerateRequest):
    from fastapi.responses import StreamingResponse as SR
    import json as _json

    def generator():
        try:
            with client.messages.stream(
                model="claude-sonnet-4-20250514",
                max_tokens=req.max_tokens,
                messages=[{"role": "user", "content": req.prompt}]
            ) as s:
                for text in s.text_stream:
                    yield f"data: {_json.dumps({'delta': text})}\n\n"
            yield "data: [DONE]\n\n"
        except anthropic.AuthenticationError:
            yield f"data: {_json.dumps({'error': 'Nieprawidłowy klucz API'})}\n\n"
        except anthropic.RateLimitError:
            yield f"data: {_json.dumps({'error': 'Limit zapytań'})}\n\n"
        except Exception as e:
            yield f"data: {_json.dumps({'error': str(e)})}\n\n"

    return SR(
        generator(),
        media_type="text/event-stream",
        headers={"Cache-Control": "no-cache", "X-Accel-Buffering": "no"}
    )


@app.get("/api/health")
def health():
    key = os.environ.get("ANTHROPIC_API_KEY", "")
    db_ok = False
    try:
        r = httpx.get(
            f"{SUPABASE_URL}/rest/v1/store?limit=1",
            headers=supa_headers(),
            timeout=5
        )
        db_ok = r.status_code in (200, 206)
    except:
        pass
    return {
        "status": "ok",
        "api_key_set": bool(key),
        "api_key_preview": key[:8] + "..." if key else "BRAK",
        "db_connected": db_ok
    }
