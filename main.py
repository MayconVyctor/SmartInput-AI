import os
from dotenv import load_dotenv
from app.services.ai_service import processar_texto_com_ia
from app.database.connection import salvar_no_banco

load_dotenv()

def run_smart_input():

    print("--- Iniciando SmartInputAI ---")

    texto_bruto = (
        "Ola, o usuario Maycon Vyctor relatou lentidao no sistema de vitoria da conquista"
        "Disse que nao consegue gerar relatorios desde as 08:00. prioridade maxima"
    )

    try:
        print(" Enviando para analise da inteligencia artificial...")
        resultado_ia = processar_texto_com_ia(texto_bruto)
        print(f"Salvando no banco de dados (Urgencia: {resultado_ia.urgencia})...")
        salvar_no_banco(resultado_ia, texto_bruto)
        print("Fluxo Finalizado com sucesso!")

    except Exception as error:
        print(f"Ocorreu um erro no fluxo: {error}")

if __name__ == "__main__":
    run_smart_input()