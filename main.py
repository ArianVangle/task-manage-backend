from fastapi import FastAPI
import uvicorn
from contextlib import asynccontextmanager
from database import create_tables, delete_tables
from router import router as tasks_router


@asynccontextmanager
async def lifespan(app: FastAPI):
    await delete_tables()
    await create_tables()
    yield
    print("Turn off")


app = FastAPI(lifespan=lifespan)
app.include_router(tasks_router)

if __name__ == '__main__':
    uvicorn.run("main:app", reload=True)
