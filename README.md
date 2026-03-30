# SmartInput AI 🧠🚀

**SmartInput** é uma solução de engenharia de software desenvolvida para automatizar a triagem e classificação de dados não estruturados. Utilizando Inteligência Artificial (LLMs), o sistema transforma entradas de texto bruto em dados estruturados prontos para persistência em bancos de dados relacionais.

## 🎯 O Problema
Processos de triagem manual são lentos, sujeitos a erros e criam gargalos operacionais. O **SmartInput** visa eliminar essa dependência, aumentando a agilidade do fluxo de dados em até 90%.

## 🛠️ Stack Tecnológica
- **Linguagem:** Python 3.11
- **IA:** OpenAI API 
- **Validação de Dados:** Pydantic 
- **Banco de Dados:** PostgreSQL
- **Infraestrutura:** Docker & Docker Compose

## ⚙️ Como Funciona
1. **Captura:** O sistema recebe um texto não estruturado (e-mails, logs, mensagens).
2. **Processamento:** Através de engenharia de prompt e integração com a API da OpenAI, as entidades-chave são extraídas.
3. **Validação:** O Pydantic valida se o JSON de retorno está conforme o contrato definido.
4. **Persistência:** Os dados validados são salvos automaticamente no PostgreSQL via `psycopg2`.

## 🐳 Execução com Docker
Para rodar o ambiente de banco de dados:
```bash
docker-compose up -d
