import uvicorn
import os
from app.app import app
from dotenv import load_dotenv

load_dotenv()

PORT = int(os.getenv("PORT", 8000))

if __name__ == "__main__":
    print(f'\033[93m Starting server in http://localhost:{PORT} ... \033[00m')

    uvicorn.run(
        app,
        host="0.0.0.0",
        port=PORT,
    )