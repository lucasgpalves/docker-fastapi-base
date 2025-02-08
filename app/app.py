import os
import uvicorn
from fastapi import FastAPI
from dotenv import load_dotenv

load_dotenv()

PORT = int(os.getenv("PORT", 8000))

app = FastAPI()

@app.get("/")
async def ping():
    return {"message": "Pong"}

def main():
    print(f'\033[93m Starting server in http://localhost:{PORT} ... \033[00m')

    uvicorn.run(
        app,
        host="0.0.0.0",
        port=PORT,
    )