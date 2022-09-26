from pydantic import BaseModel

class Faves(BaseModel):
    user: str
    manga_id: str
