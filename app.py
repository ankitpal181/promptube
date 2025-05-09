import re, json
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from mangum import Mangum
from services.llm_service import generate_queries_service
from services.auth_service import AuthService

app = FastAPI()

class Request(BaseModel):
    email: str
    prompt: str

@app.post("/generate-queries")
async def generate_queries(request: Request):
    try:
        if not AuthService().verify_user(request.email): raise Exception("User not subscribed")

        response = generate_queries_service(request.prompt)
        queries = re.split(r"\d+\.\s", response)
        filtered_queries = []

        for query in queries:
            if query: filtered_queries.append(query.strip())

        return {
            "response": filtered_queries
        }
    except Exception as ex:
        print(ex)
        return {
            "error": str(ex)
        }

# This is the Lambda handler
handler = Mangum(app)

# Temp directory setup for writable files
with open("data.json", "r") as file:
    data = json.load(file)

with open("/tmp/data.json", "w") as file:
    json.dump(data, file)
