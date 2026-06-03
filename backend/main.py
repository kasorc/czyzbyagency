from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from fastapi.staticfiles import StaticFiles
from fastapi.responses import FileResponse
from pydantic import BaseModel
from typing import Optional, Any
import anthropic
import os
import json
import psycopg2
import psycopg2.extras
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


# ── BAZA DANYCH ──────────────────────────────────────────────
def get_conn():
    db_url = os.environ.get("DATABASE_URL")
    if not db_url:
        raise HTTPException(status_code=500, detail="Brak zmiennej DATABASE_URL")
    return psycopg2.connect(db_url)

def init_db():
    """Tworzy tabele jeśli nie istnieją."""
    try:
        db_url = os.environ.get("DATABASE_URL")
        if not db_url:
            return  # bez bazy nie crashujemy przy starcie
        conn = psycopg2.connect(db_url)
        cur = conn.cursor()
        cur.execute("""
            CREATE TABLE IF NOT EXISTS store (
                key TEXT PRIMARY KEY,
                value JSONB NOT NULL,
                updated_at TIMESTAMPTZ DEFAULT NOW()
            )
        """)
        conn.commit()
        cur.close()
        conn.close()
        print("DB: tabele gotowe")
    except Exception as e:
        print(f"DB init warning: {e}")

# Inicjalizacja przy starcie
init_db()


# ── MODELE ──────────────────────────────────────────────────
class GenerateRequest(BaseModel):
    prompt: str
    max_tokens: int = 1200

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
        conn = get_conn()
        cur = conn.cursor(cursor_factory=psycopg2.extras.RealDictCursor)
        cur.execute("SELECT value FROM store WHERE key = %s", (key,))
        row = cur.fetchone()
        cur.close()
        conn.close()
        if row is None:
            return StoreGetResponse(key=key, value=None)
        return StoreGetResponse(key=key, value=row["value"])
    except HTTPException:
        raise
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@app.post("/api/store")
def store_set(req: StoreSetRequest):
    try:
        conn = get_conn()
        cur = conn.cursor()
        cur.execute("""
            INSERT INTO store (key, value, updated_at)
            VALUES (%s, %s, NOW())
            ON CONFLICT (key) DO UPDATE
              SET value = EXCLUDED.value,
                  updated_at = NOW()
        """, (req.key, json.dumps(req.value)))
        conn.commit()
        cur.close()
        conn.close()
        return {"ok": True}
    except HTTPException:
        raise
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


# ── ENDPOINTY – AI ───────────────────────────────────────────
@app.post("/api/generate", response_model=GenerateResponse)
def generate(req: GenerateRequest):
    try:
        response = client.messages.create(
            model="claude-sonnet-4-20250514",
            max_tokens=req.max_tokens,
            messages=[{"role": "user", "content": req.prompt}]
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
        raise HTTPException(status_code=401, detail="Nieprawidłowy klucz API. Sprawdź zmienną ANTHROPIC_API_KEY.")
    except anthropic.RateLimitError:
        raise HTTPException(status_code=429, detail="Przekroczono limit zapytań. Poczekaj chwilę.")
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


@app.get("/api/health")
def health():
    key = os.environ.get("ANTHROPIC_API_KEY", "")
    db_ok = False
    try:
        db_url = os.environ.get("DATABASE_URL", "")
        if db_url:
            conn = psycopg2.connect(db_url)
            conn.close()
            db_ok = True
    except:
        pass
    return {
        "status": "ok",
        "api_key_set": bool(key),
        "api_key_preview": key[:8] + "..." if key else "BRAK",
        "db_connected": db_ok
    }
