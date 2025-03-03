# Added this file just for reference
from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def home():
    return {"message": "FastAPI is running!"}

# Run it in PyCharm Terminal: uvicorn main:app --host 0.0.0.0 --port=5000