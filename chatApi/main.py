from fastapi import FastAPI
from chatApi.routes.user import router as user_router
from chatApi.routes.thread import router as thread_router
from chatApi.routes.threadHeadings import router as threadHeadings_router
from chatApi.routes.patternIdentify import router as patternIdentify_router


app = FastAPI()
app.include_router(user_router,prefix="/users")
app.include_router(thread_router,prefix="/threads")
app.include_router(threadHeadings_router,prefix="/threadHeadings")
app.include_router(patternIdentify_router,prefix="/patternIdentify")
