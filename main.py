from langchain_openai import ChatOpenAI
from dotenv import load_dotenv
import os

load_dotenv()
api_key = os.getenv("OPENAI_API_KEY")

numero_dias = 7
numero_criancas = 5
atividade = "praia"

prompt = (f"Crie um roteiro de viagens, para um periodo de {numero_dias}, para uma familia com "
          f"{numero_criancas} que busca atividades relacionadas a {atividade}")

modelo = ChatOpenAI(
    model = "gpt-4.0",
    temperature =0.5,
    api_key=api_key
)

resposta= modelo.invoke(prompt)
print(resposta)