# 🦜🔗 LangChain com Python — Ferramentas com LLM OpenAI

Repositório do curso **LangChain e Python: criando ferramentas com a LLM OpenAI**, cobrindo desde os fundamentos do LangChain até a criação de agentes e pipelines inteligentes com a API da OpenAI.

---

## 🚀 Tecnologias

- [Python 3.11+](https://www.python.org/)
- [LangChain](https://www.langchain.com/)
- [LangGraph](https://langchain-ai.github.io/langgraph/)
- [OpenAI API](https://platform.openai.com/)
- [FAISS](https://github.com/facebookresearch/faiss)
- [python-dotenv](https://pypi.org/project/python-dotenv/)

---

## ⚙️ Configuração do Ambiente

### 1. Clonar o repositório

```bash
git clone https://github.com/seu-usuario/seu-repositorio.git
cd seu-repositorio
```

### 2. Criar e ativar o ambiente virtual

**Windows:**
```bash
python -m venv langchain
langchain\Scripts\activate
```

**Mac/Linux:**
```bash
python3 -m venv langchain
source langchain/bin/activate
```

### 3. Instalar as dependências

```bash
pip install -r requirements.txt
```

### 4. Configurar a chave da OpenAI

Crie um arquivo `.env` na raiz do projeto:

```env
OPENAI_API_KEY="sua-chave-aqui"
```

> ⚠️ Nunca suba o arquivo `.env` para o GitHub. Ele já está listado no `.gitignore`.

---

## 📁 Estrutura do Projeto

```
📦 curso-langchain
 ┣ 📜 main.py
 ┣ 📜 requirements.txt
 ┣ 📜 .env              ← criado localmente (não versionado)
 ┣ 📜 .gitignore
 ┗ 📜 README.md
```

---

## 📚 Conteúdo do Curso

- Introdução ao LangChain e LLMs
- Integração com a API da OpenAI
- Criação de prompts dinâmicos
- Chains e pipelines de processamento
- Memória e histórico de conversas
- Agentes inteligentes com LangGraph
- Busca semântica com FAISS
- Boas práticas e deploy

---

## 🔑 Pré-requisitos

- Python 3.11 ou superior
- Conta na OpenAI com créditos de API disponíveis → [platform.openai.com](https://platform.openai.com/settings/billing)

---

## 📄 Licença

Este projeto é apenas para fins educacionais.
