from fastapi import FastAPI, HTTPException
from app.services.ai_service import processar_texto_com_ia
from app.models.schema import DadosTriagem


app = FastAPI()

@app.get("/")
def home():
    return {"status": "SmartInputAI API Rodando"}

@app.post("/triagem", response_model=DadosTriagem)
def realizar_triagem(texto_bruto: str):
    try:
  
        resultado = processar_texto_com_ia(texto_bruto)
        

        return resultado
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))