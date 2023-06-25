from fastapi import FastAPI

from core.database.depends import init_db
from core.users.router import router as users_router

app = FastAPI()


# Add routers
app.include_router(users_router)


# Create tables
@app.on_event("startup")
async def on_startup():
    await init_db()
