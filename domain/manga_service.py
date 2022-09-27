from pydantic import BaseModel


class MangaService(BaseModel):
    manga_id: str
    service_name: str
    url: str
