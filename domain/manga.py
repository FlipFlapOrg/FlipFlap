from pydantic import BaseModel

class Manga(BaseModel):
    manga_id: str
    title: str
    author: str
