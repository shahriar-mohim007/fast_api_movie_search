from sqlalchemy import create_engine
from app.movie_search.model.models import Base
from sqlalchemy.orm import sessionmaker

DATABASE_URL = "postgresql://postgres:postgres@localhost:5432/movie"

engine = create_engine(DATABASE_URL, echo=True,future=True)
SessionLocal = sessionmaker(autocommit=False, autoflush=False,bind=engine)

Base.metadata.create_all(bind=engine)

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

#echo=True: When set to True, it enables logging of all the SQL statements generated by SQLAlchemy.
#This means each query executed by the engine will be printed to the console or log.
#This is helpful for debugging or monitoring the SQL queries being executed by your application.


# In this case, by setting future=True, you are preparing your codebase for
# SQLAlchemy 2.x-style functionality while still potentially running on 1.x

# 2.x: Full native asynchronous support for databases like PostgreSQL and MySQL using async_engine,
# AsyncSession, and await. This allows you to use SQLAlchemy effectively with async frameworks like FastAPI.


