from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from fastapi.staticfiles import StaticFiles
from fastapi.responses import FileResponse
from pydantic import BaseModel
from typing import Optional
import anthropic
import os
from pathlib import Path

app = FastAPI(title="Social AI API")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

client = anthropic.Anthropic(api_key=os.environ.get("ANTHROPIC_API_KEY"))

# Ścieżka do frontendu – działa zarówno lokalnie jak i na Railway
BASE_DIR = Path(__file__).parent.parent
FRONTEND_DIR = BASE_DIR / "frontend"

app.mount("/static", StaticFiles(directory=str(FRONTEND_DIR)), name="static")

@app.get("/")
def root():
    return FileResponse(str(FRONTEND_DIR / "index.html"))


# ── MODELE ──────────────────────────────────────────────────
class GenerateRequest(BaseModel):
    prompt: str
    max_tokens: int = 1200

class GenerateResponse(BaseModel):
    content: str
    usage: Optional[dict] = None


# ── ENDPOINTY ───────────────────────────────────────────────
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
    return {
        "status": "ok",
        "api_key_set": bool(key),
        "api_key_preview": key[:8] + "..." if key else "BRAK"
    }
