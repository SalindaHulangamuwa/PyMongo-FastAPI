from chatApi.db.dataBase import users_collection
from chatApi.models.user import UserMetaData

def create_update_user(user: UserMetaData):
    userData= user.dict()
    users_collection.update_one(
        {"userId": userData["userId"]},
        {"$set": userData},
        upsert=True
    )
    return {"message": "User data updated successfully"}