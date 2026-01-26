
from pydantic import BaseModel

class InstanceRequest(BaseModel):
    ami_id: str
    instance_type: str
    key_name: str
    instance_name: str
    min_count: int = 1
    max_count: int = 1
    
