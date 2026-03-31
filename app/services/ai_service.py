import os
from openai import OpenAI
from app.models.schema import DadosTriagem

def processar_texto_com_ia(texto: str) -> DadosTriagem:
    client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))
    response = client.beta.chat.completions.parse(
        model="gpt-4o-mini",
        messages=[
            {
                "role": "system",
                "content": (
                    "Você é um especialista em triagem de suporte técnico. Extraia as informações do texto de forma estruturada."
                )
            },
            {
                "role": "user",
                "content": texto
            }
        ],
        response_format=DadosTriagem
    )

    return response.choices[0].message.content