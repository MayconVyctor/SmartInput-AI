from pydantic import BaseModel
from typing import List

class DadosTriagem(BaseModel):
    tarefa: str
    categoria: str
    urgencia: str
    entidades: List[str]