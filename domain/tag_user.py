from pydantic import BaseModel

class TagUser(BaseModel):
    user_id: str
    tag: str
