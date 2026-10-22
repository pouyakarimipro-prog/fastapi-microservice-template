from fastapi import FastAPI, status
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI(
    title="Core Service API",
    version="1.0.0",
    docs_url="/docs",
    redoc_url=None
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/healthz", status_code=status.HTTP_200_OK)
async def health_check():
    return {"status": "ok", "service": "healthy"}

@app.get("/api/v1/info")
async def service_info():
    return {
        "version": "1.0.0",
        "runtime": "python-async"
    }
