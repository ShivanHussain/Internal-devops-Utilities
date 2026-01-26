from fastapi import FastAPI # type: ignore #importing FastAPI class
from routers import metrics, aws , hello

app = FastAPI(
    title="Internal Devops Utilities",
    description="This is an Internal API utilities App for monitoring metrics, AWS usage , log Nalysis etc.",
    version="1.0.0",
    docs_url="/docs",
    redoc_url="/redoc"
)





app.include_router(hello.router)
app.include_router(metrics.router)
app.include_router(aws.router, prefix="/aws")