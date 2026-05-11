from langchain_openai import ChatOpenAI
from langchain.prompts import PromptTemplate
from langchain_core.output_parsers import JsonOutputParser, StrOutputParser
from pydantic import Field, BaseModel
from dotenv import load_dotenv
from langchain.globals import set_debug
import os

set_debug(True)

# carrega as variáveis do arquivo .env
load_dotenv()

# acessa a chave de uma API de forma segura
api_key = os.getenv("OPENAI_API_KEY")

# verificação se a chave da API existe
if api_key is None:
    raise ValueError("A chave da API não foi definida no .env")

print("Chave carregada com sucesso!")

class Destino(BaseModel):
    cidade:str = Field("A cidade recomendada para visitar")
    motivo:str = Field("Motivo pelo qual é interessante visitar essa cidade")

class Restaurantes(BaseModel):
    cidade:str = Field("A cidade recomendada para visitar")
    restaurantes:str = Field("restaurantes recomendados para visitar na cidade")

parseador_destino = JsonOutputParser(pydantic_object=Destino)
parseador_restaurantes = JsonOutputParser(pydantic_object=Restaurantes)

prompt_cidade = PromptTemplate(
    template="""
    Sugira uma cidade dado o meu interesse por {interesse}.
    {formato_de_saída}
    """,
    input_variables=["interesse"],
    variaveis_parciais={"formato_de_saída":parseador_destino.get_format_instructions()}
)

prompt_restaurantes = PromptTemplate(
    template="""
    Sugira restaurantes populares entre locais em {cidade}.
    {formato_de_saída}
    """,
    variaveis_parciais={"formato_de_saída":parseador_restaurantes.get_format_instructions()}
)

prompt_cultural = PromptTemplate(
    template="Sugira atividades e locais culturais em {cidade}"
)

modelo = ChatOpenAI(
    model = "gpt-4.0",
    temperature =0.5,
    api_key=api_key
)

cadeia_1 = prompt_cidade | modelo | parseador_destino
cadeia_2 = prompt_restaurantes | modelo | parseador_restaurantes
cadeia_3 = prompt_cultural | modelo | StrOutputParser()

cadeia = (cadeia_1 |     cadeia_2 | cadeia_3)

resposta= cadeia.invoke(
    {
    "interesse": "praias"
    }
)
print(resposta)