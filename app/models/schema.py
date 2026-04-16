from pydantic import BaseModel
from typing import List
from pydantic import BaseModel, Field
from typing import List

class DadosTriagem(BaseModel):
    tarefa: str = Field(..., description="Resumo sucinto da solicitação extraída do texto")
    categoria: str = Field(..., description="Classificação técnica (ex: Hardware, Software, Acesso)")
    urgencia: str = Field(..., description="Nível de prioridade: Baixa, Media ou Alta")
    entidades: List[str] = Field(..., description="Nomes de pessoas, locais ou sistemas mencionados")