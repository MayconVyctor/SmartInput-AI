from fastapi import FastAPI, Request, logger
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import JSONResponse
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


@app.exception_handler(Exception)
async def gerenciar_erro_global(request: Request, exc: Exception):
    logger.error(f"Erro inesperado: {str(exc)}")
    
    return JSONResponse(
        status_code=500,
        content={
            "sucesso": False,
            "mensagem": "Ops! Ocorreu um erro interno no SmartInputAI.",
            "detalhe": str(exc) 
        }
    )

app.include_router(api_router, prefix="/api/v1")

@app.get("/")
def home():
    return {"status": "SmartInputAI API Rodando"}

@app.get("/", tags=["Healthcheck"])
def health_check():
    return {
        "status": "online",
        "app": "SmartInputAI",
        "version": "1.0.0",
        "api_docs": "/docs"
    }