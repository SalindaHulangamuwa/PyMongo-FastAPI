from chatApi.db.dataBase import users_collection, threads_collection
import uuid
from chatApi.models.user import UserMetaData

def create_update_user(user: UserMetaData):
    userData = user.dict(by_alias=True)
    
    existing_user = users_collection.find_one({"_id": userData["_id"]})
    if existing_user and existing_user.get("organizationId") != userData["organizationId"]:
        return (f"User {userData['_id']} already exists with a different organizationId. Cannot update with new organizationId.")

    users_collection.update_one(
        {"_id": userData["_id"]}, 
        {"$set": {
            '_id': userData["_id"], 
            "organizationId": userData["organizationId"], 
            "policyIds": userData["policyIds"], 
            "evidenceIds": userData["evidenceIds"], 
            "hazardIds": userData["hazardIds"], 
            "incidentIds": userData["incidentIds"]
        }}, 
        upsert=True
    )
    print(userData)

    existing_thread = threads_collection.find_one({"userId": userData["_id"]})
    if not existing_thread:
        threads_collection.insert_one({
            "_id": str(uuid.uuid4()), 
            "userId": userData["_id"], 
            "threadHeading": userData["threadHeading"]
        })
        print("inserted")
    else:
        threads_collection.update_one(
            {"userId": userData["_id"]},
            {"$set": {"threadHeading": userData["threadHeading"]}}
        )
        print("updated")
    
    threadHeading = threads_collection.find_one(
        {"userId": userData["_id"]}, 
        {"_id": 1, "threadHeading": 1}
    )
    
    print(threadHeading)
    
    if not threadHeading.get("threadHeading"):
        return ("didn't have a thread Heading in", threadHeading["_id"])
    else:
        insert_result = threads_collection.insert_one({
            "_id": str(uuid.uuid4()), 
            "userId": userData["_id"], 
            "threadHeading": None
        })
        return ("new thread_id", insert_result.inserted_id)