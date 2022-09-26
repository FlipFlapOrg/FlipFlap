from pydantic import BaseModel

class Bookmark(BaseModel):
    manga_id: str
    user_id: str
