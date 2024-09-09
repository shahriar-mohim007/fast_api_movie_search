from sqlalchemy.orm import Session
from .models import User,SearchLog,FavoriteMovie
class MovieRepository:
    def __init__(self,db: Session):
        self.session = db

    def create_user(self,data):
        existing_user = self.session.query(User).filter(User.email == data.get("email")).first()
        if existing_user:
            return None
        new_user = User(**data)
        self.session.add(new_user)
        self.session.commit()
        self.session.refresh(new_user)
        return new_user

    def match_email_password(self,data):
        return self.session.query(User).filter(User.email == data.get("email"),
                                               User.password==data.get("password")).first()
    
    def movie_already_exist(self,imdb_id):
        return self.session.query(FavoriteMovie).filter_by(imdb_id=imdb_id).first()
    
    def add_favorite_movie(self,user_id: int, imdb_id: str):
        movie = self.movie_already_exist(imdb_id)
        if movie:
           return None
        user = self.session.query(User).filter_by(id=user_id).first()
       
        if not movie:
            fav_movie = FavoriteMovie(user_id=user_id, imdb_id=imdb_id)
            user.movies.append(fav_movie)

            self.session.add(user)
            self.session.commit()
        return user.movies

    def create_log(self,data):
        log = SearchLog(**data)
        self.session.add(log)
        self.session.commit()
        self.session.refresh(log)
        return log
