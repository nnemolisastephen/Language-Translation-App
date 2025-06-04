from fastapi import FastAPI
import os
from langchain_groq import ChatGroq
from dotenv import load_dotenv
from langserve import add_routes
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser
load_dotenv()

groq_api_key = os.getenv("GROQ_API_KEY")
mistral_model = ChatGroq(model="gemma2-9b-it",groq_api_key=groq_api_key)

prompt_template = "Translate from English to {language}"

prompt = ChatPromptTemplate.from_messages([("system",prompt_template),("user","{text}")])
parser = StrOutputParser()

chain = prompt | mistral_model | parser

app = FastAPI(
    title = "LangchainAPI",
    description = "An application for Language Translation",
    version='1.0'
)

add_routes(
    app,
    chain,
    path="/chain"
)

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app,host = "127.0.0.1", port = 8000)
