from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from app.services.ai_service import processar_texto_com_ia
from app.models.schema import DadosTriagem


app = FastAPI(title="SmartInputAI API")
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
@app.get("/")
def home():
    return {"status": "SmartInputAI API Rodando"}

