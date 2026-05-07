from langchain_openai import ChatOpenAI
from langchain.prompts import PromptTemplate
from dotenv import load_dotenv
import os

# carrega as variáveis do arquivo .env
load_dotenv()

# acessa a chave de uma API de forma segura
api_key = os.getenv("OPENAI_API_KEY")

# verificação se a chave da API existe
if api_key is None:
    raise ValueError("A chave da API não foi definida no .env")

print("Chave carregada com sucesso!")

numero_dias = 7
numero_criancas = 5
atividade = "praia"

modelo_de_prompt = PromptTemplate(
    template="""
    Crie um roteiro de viagem de {dias} dias,
    para uma familia com {numero_criancas} criancas,
    que gostam de {atividade}
    """
)

prompt = modelo_de_prompt.format(
    dias = numero_dias,
    numero_criancas = numero_criancas,
    atividade = atividade
)

print("Prompt : \n", prompt)

modelo = ChatOpenAI(
    model = "gpt-4.0",
    temperature =0.5,
    api_key=api_key
)

resposta= modelo.invoke(prompt)
print(resposta)