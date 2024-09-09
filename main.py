import logging
import uvicorn
from fastapi import FastAPI
from app.movie_search.router import move_router

logger =logging.getLogger(__name__)

app = FastAPI(
    title="Movie Search",
    version="1.0.0",
)
app.include_router(move_router)

if __name__ == '__main__':
    uvicorn.run("main:app", port=8080, host="0.0.0.0", reload=True, log_level="info")