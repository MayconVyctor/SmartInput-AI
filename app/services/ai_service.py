import os
import json
import time
import requests
from dotenv import load_dotenv
from app.models.schema import DadosTriagem

load_dotenv()

def processar_texto_com_ia(texto: str) -> DadosTriagem:
    api_key = os.getenv("GOOGLE_API_KEY")
    
    modelos_possiveis = [
        "gemini-flash-lite-latest",
        "gemini-pro-latest",
        "gemini-2.5-flash-lite",
    ]
    
    headers = {'Content-Type': 'application/json'}
    payload = {
        "contents": [{
            "parts": [{
                "text": (
                    "Extraia os dados do texto a seguir em formato JSON. "
                    "Use exatamente estas chaves: tarefa, categoria, urgencia, entidades. "
                    f"Texto: {texto}"
                )
            }]
        }],
        "generationConfig": {
            "response_mime_type": "application/json"
        }
    }
    
    for modelo in modelos_possiveis:
        url = f"https://generativelanguage.googleapis.com/v1beta/models/{modelo}:generateContent?key={api_key}"
        print(f"🔄 Tentando modelo: {modelo}")
        
        response = requests.post(url, headers=headers, json=payload)
        
        if response.status_code == 200:
            print(f"✅ Sucesso com {modelo}!")
            res_json = response.json()
            texto_resposta = res_json['candidates'][0]['content']['parts'][0]['text']
            dados_dict = json.loads(texto_resposta)
            return DadosTriagem(**dados_dict)
            
        elif response.status_code == 404:
            print(f"  ⚠️  {modelo} não disponível, tentando próximo...")
            continue
            
        elif response.status_code == 429:
            delay = 30
            details = response.json().get('details', [])
            for detail in details:
                if detail.get('@type') == "type.googleapis.com/google.rpc.RetryInfo":
                    retry_str = detail.get('retryDelay', '30s')
                    delay = int(''.join(filter(str.isdigit, retry_str)) or 30)
                    break
            print(f"⏳ Quota esgotada para {modelo}. Aguardando {delay}s...")
            time.sleep(delay)
            continue  
            
        else:
            print(f"  Erro inesperado com {modelo}: {response.status_code}")
            continue
    
    raise Exception("Nenhum modelo funcionou. Verifique quota em: https://aistudio.google.com/app/quota")