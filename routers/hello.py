from fastapi import APIRouter, HTTPException # type: ignore
from services.hello_service import hello

router = APIRouter()

@router.get("/", status_code=200)
def get_hello():
    try: 
        hello_data = hello()
        return hello_data
    except:
        raise HTTPException(
            status_code=500,
            detail="Internal Server Error"
        )