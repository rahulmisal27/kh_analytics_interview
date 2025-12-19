from fastapi import FastAPI
from api import router as api_router

app = FastAPI()

if __name__ == "__main__":
    import uvicorn

    app.include_router(api_router, prefix="/api")

    uvicorn.run(app, host="localhost", port=8000)
