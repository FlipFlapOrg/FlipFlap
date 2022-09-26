from handler.schema import MangaResponse


# GET /manga/recommend
def get_recommendation(user_id: str) -> MangaResponse:
    return MangaResponse(
        manga_id="4ed8e4ab-50c2-4e87-abf1-ebf2cc87dcf1",
        title="One Piece",
        author="Eiichiro Oda",
        image_url=["https://i.pinimg.com/originals/4c/50/38/4c50386d57d207a960058fcc8a5609a8.jpg",
                   "https://qph.cf2.quoracdn.net/main-qimg-835ac26be15950837045ba53cca30845-lq"],
        tags=["action", "adventure", "comedy", "fantasy", "shounen"],
        is_faved=True,
        is_bookmarked=False
    )
