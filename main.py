import os

import pandas as pd
from dotenv import load_dotenv
from fastapi import FastAPI, HTTPException
from fastapi.staticfiles import StaticFiles
from langchain.chains import RetrievalQA
from langchain_community.embeddings import SentenceTransformerEmbeddings
from langchain_community.llms import HuggingFaceHub
from langchain_community.vectorstores import FAISS

from schemas import UserMemory, UserQuery


load_dotenv()

app = FastAPI()

cocktails_df = pd.read_csv("data/cocktails.csv")
cocktails_df["combined_text"] = (cocktails_df["name"] +
                                 " " + cocktails_df["ingredients"] + " " + cocktails_df["instructions"])
cocktails = cocktails_df.to_dict("records")


llm = HuggingFaceHub(repo_id="gpt2",
                     model_kwargs={"temperature":0.5, "max_new_tokens":200},
                     huggingfacehub_api_token=os.environ["HUGGINGFACE_API_TOKEN"])
embeddings = SentenceTransformerEmbeddings(model_name="all-mpnet-base-v2")
db = FAISS.from_texts(cocktails_df["combined_text"].tolist(), embeddings)

qa = RetrievalQA.from_chain_type(llm=llm, chain_type="stuff", retriever=db.as_retriever())


@app.get("/")
async def root():
    return {"message": "Hi :)"}

@app.post("/ask/")
async def ask(query: UserQuery):
    try:
        response = qa.run(query.question)
        return {"response": response}
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e)) from e

@app.post("/store_mem/")
async def store_mem(memory: UserMemory):
    try:
        combined_memory = " ".join(memory.ingredients) + " ".join(memory.cocktails)
        db.add_texts([combined_memory], embeddings=embeddings)
        return {"status": "success"}
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e)) from e


app.mount("/static", StaticFiles(directory="."), name="static")
