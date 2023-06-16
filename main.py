from fastapi import FastAPI
import uvicorn

if __name__ == "__main__":
  uvicorn.run("server.api:app", host="0.0.0.0", port=8000, reload=True)

app = FastAPI()

@app.get("/")
def hello_api():
    return {"msg":"Hello API"}