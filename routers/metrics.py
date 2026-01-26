from fastapi import APIRouter, HTTPException # type: ignore
from services.metrics_service import get_system_metrics

router = APIRouter()

@router.get("/metrics", status_code=200)
def get_metrics():
    try: 
        metric = get_system_metrics()
        return metric
    except:
        raise HTTPException(
            status_code=500,
            detail="Internal Server Error"
        )