from fastapi import APIRouter, HTTPException
from app.services.ai_service import processar_texto_com_ia
from app.models.schema import DadosTriagem

router = APIRouter(tags=["Triagem"])

@router.post("/triagem", response_model=DadosTriagem)
def realizar_triagem(texto_bruto: str):
    try:
        return processar_texto_com_ia(texto_bruto)
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))