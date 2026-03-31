import os
import psycopg2
from dotenv import load_dotenv
from psycopg2.extras import Json

def salvar_no_banco(resultado, original):
    load_dotenv()
    try:
        conn = psycopg2.connect(
            host=os.getenv("DB_HOST"),
            port=os.getenv("DB_PORT"),
            database=os.getenv("DB_NAME"),
            user=os.getenv("DB_USER"),
            password=os.getenv("DB_PASS")
        )
        cursor = conn.cursor()

        insert_query = """
        INSERT INTO triagem_ia (tarefa, categoria, urgencia, entidades, texto_original)
        VALUES (%s, %s, %s, %s, %s)
        """
        cursor.execute(insert_query, (
            resultado.tarefa,
            resultado.categoria,
            resultado.urgencia,
            Json(resultado.entidades),
            original
        ))

        conn.commit()
        print("Dados salvos com sucesso no PostgreSQL via Docker")

    except Exception as error:
        print(f"Erro ao salvar no banco: {error}")

    finally:
        if 'conn' in locals():
            cursor.close()
            conn.close()