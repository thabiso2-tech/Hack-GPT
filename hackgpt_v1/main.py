from fastapi import FastAPI
from pydantic import BaseModel
from orchestrator import run_hackgpt

app = FastAPI(title="HackGPT v1 by Lowani")

class Request(BaseModel):
    query: str

@app.post("/analyze")
def analyze(req: Request):
    return {"result": run_hackgpt(req.query)}
