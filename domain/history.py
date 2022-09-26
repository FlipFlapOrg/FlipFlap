from pydantic import BaseModel

class History(BaseModel):
    manga_id: str
    user_id: str
