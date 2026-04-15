from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.api.endpoints import router as api_router

app = FastAPI(title="SmartInputAI API",
    description="API de triagem inteligente utilizando modelos Gemini",
    version="1.0.0",
    contact={
        "name": "Maycon Vyctor",
        "url": "https://github.com/MayconVyctor",
    }
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(api_router, prefix="/api/v1")

@app.get("/")
def home():
    return {"status": "SmartInputAI API Rodando"}