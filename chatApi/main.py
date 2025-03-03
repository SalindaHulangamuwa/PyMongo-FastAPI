from fastapi import FastAPI
from chatApi.routes.user import router as user_router
from chatApi.routes.thread import router as thread_router


app = FastAPI()
app.include_router(user_router,prefix="/users")
app.include_router(thread_router,prefix="/threads")
