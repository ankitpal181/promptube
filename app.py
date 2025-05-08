import re
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from mangum import Mangum
from llm_service import generate_queries_service

app = FastAPI()

class Request(BaseModel):
    prompt: str

@app.post("/generate-queries")
async def generate_queries(request: Request):
    response = generate_queries_service(request.prompt)
    queries = re.split(r"\d+\.\s", response)
    filtered_queries = []

    for query in queries:
        if query: filtered_queries.append(query.strip())

    return {
        "response": filtered_queries
    }

# This is the Lambda handler
handler = Mangum(app)
