
from sqlalchemy import Column, Integer, String, ForeignKey,Text
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class User(Base):
    __tablename__ = 'user'
    id = Column(Integer, autoincrement=True, primary_key=True)
    fullname = Column(String(200), nullable=False)
    email = Column(String(100), nullable=False, unique=True, index=True)
    password = Column(String(128), nullable=False)
    movies = relationship('FavoriteMovie', backref='user', lazy='joined')
    search_logs = relationship("SearchLog", back_populates="user")

class FavoriteMovie(Base):
    __tablename__ = 'favorite_movie'
    id = Column(Integer, autoincrement=True, primary_key=True)
    user_id = Column(Integer, ForeignKey('user.id'), nullable=False, index=True)
    imdb_id = Column(String(100), nullable=False)


class SearchLog(Base):
    __tablename__ = 'search_log'

    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey('user.id'), nullable=False)
    query = Column(Text)

    user = relationship("User", back_populates="search_logs")