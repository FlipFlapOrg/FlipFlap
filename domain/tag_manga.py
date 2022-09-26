from pydantic import BaseModel

class TagManga(BaseModel):
    manga_id: str
    tag: str
