
from fastapi import HTTPException, status
from repository.faves import faves_db

from handler.schema import FaveRequest


# POST /users/{user_id}/faves
def add_user_fave(req: FaveRequest, user_id: str):
    res = faves_db.add_faves(user_id=user_id, manga_id=req.manga_id)
    if res == False:
        raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
                            detail="Failed to add fave.")
    return None


# DELETE /users/{user_id}/faves
def remove_user_fave(req: FaveRequest, user_id: str):
    faves_db.delete_faves(user_id=user_id, manga_id=req.manga_id)
    return None
