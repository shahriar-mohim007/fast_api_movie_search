import logging
logger =logging.getLogger(__name__)

from .schema import RegisterRequest,RegisterResponse,LoginRequest,FavouriteMovieRequest
from sqlalchemy.orm import Session
from .model.repositories import MovieRepository
from .token import encode,User
from .search import search_movie


class UserController:
    def __init__(self):
        self.repository = None

    def create_user(self,dto: RegisterRequest,db: Session):
        self.repository = MovieRepository(db)
        user_data = self.repository.create_user(dto.model_dump())
        if not user_data:
            return {
                'error': 'User with this email already exists'
            }
        return RegisterResponse(**
            {
                "id": user_data.id,
                "fullname": user_data.fullname,
                "email": user_data.email,
            }
        )


class LoginController:
    def __init__(self):
        self.repository = None

    def create_token(self,dto: LoginRequest,db: Session):
        self.repository = MovieRepository(db)
        user_data = self.repository.match_email_password(dto.model_dump())
        if not user_data:
            return {"message": "User Not Found"}

        token = encode({
            "id": user_data.id,
            "fullname": user_data.fullname,
            "email": user_data.email,
        })

        return {"access_token": token}

class SearchController:
     def __init__(self):
        self.repository = None
     
     def search_movies(self,title,page,db: Session,user):
         self.repository = MovieRepository(db)
         movies = search_movie(title,page)
         dto = {
            "user_id": user.id,
            "query": title
         }
         log = self.repository.create_log(dto)
         logger.info({"search log":log})
         return movies

class FavouriteMovieController:
    def __init__(self):
        self.repository = None
    
    def add_favourite(self,db: Session,dto:FavouriteMovieRequest,user):
        self.repository = MovieRepository(db)
        movies = self.repository.add_favorite_movie(user.id,dto.imdb_id)
        if not movies:
           return {"message": "Movie already added"}
        imdb_ids = [movie.imdb_id for movie in movies]
        response = {'data': imdb_ids}
        return response



