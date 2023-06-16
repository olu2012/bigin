from fastapi import FastAPI
import uvicorn



app = FastAPI()

@app.get("/")
def hello_api():
    return {"msg":"Hello API"}