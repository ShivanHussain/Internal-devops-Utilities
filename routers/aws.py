from fastapi import APIRouter, HTTPException # type: ignore
from schema.ec2_instance import InstanceRequest
from services.aws_service import get_bucket_info, get_ec2_info , get_iam_users, create_ec2_instacne

router = APIRouter()

@router.get("/s3", status_code=200)
def get_bucket():
    try: 
        bucket_info = get_bucket_info()
        return bucket_info
    except:
        raise HTTPException(
            status_code=500,
            detail="Internal Server Error"
        )
    

@router.get("/ec2", status_code=200)
def get_instances():
    try: 
        instance_info = get_ec2_info()
        return instance_info
    except:
        raise HTTPException(
            status_code=500,
            detail="Internal Server Error"
        )
    

@router.get("/iam", status_code=200)
def get_users_info():
    try: 
        users_info = get_iam_users()
        return users_info
    except:
        raise HTTPException(
            status_code=500,
            detail="Internal Server Error"
        )
    

@router.post("/create-instance", status_code=200)
def ec2_instance_create(request: InstanceRequest):
    try:
        instance_info = create_ec2_instacne(request)
        return instance_info

    except Exception as e:
        raise HTTPException(
            status_code=500,
            detail=str(e)
        )
    


    

