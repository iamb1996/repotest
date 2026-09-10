from fastapi import FastAPI

app = FastAPI(
    title="Azure FastAPI App",
    description="My first FastAPI application deployed on Azure Container Apps",
    version="1.0.0"
)


@app.get("/")
def home():
    return {
        "message": "Hello Azure Container Apps!",
        "framework": "FastAPI",
        "status": "running"
    }


@app.get("/health")
def health():
    return {
        "status": "healthy"
    }