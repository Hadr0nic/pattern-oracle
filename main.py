from fastapi import FastAPI

app = FastAPI(title="Pattern Oracle")

@app.get("/")
def home():
    return {"message": "Pattern Oracle is running!"}