from repository.history import history_db

# POST /user/{user_id}/history
def add_history(user_id: str, manga_id: str):
    return history_db.add_history_user(manga_id=manga_id, user_id=user_id)
