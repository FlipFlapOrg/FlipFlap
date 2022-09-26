from pydantic import BaseModel

class TagUser(BaseModel):
    user: str
    manga_id: str
