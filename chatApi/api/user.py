from chatApi.db.dataBase import users_collection
from chatApi.models.user import UserMetaData

def create_update_user(user: UserMetaData):
    userData = user.dict(by_alias=True)
    
    users_collection.update_one(
        {"_id": userData["_id"]}, 
        {"$set": userData},
        upsert=True
    )
    
    return {"message": "User data updated successfully"}
