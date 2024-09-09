import logging
logger =logging.getLogger(__name__)

from fastapi import FastAPI, Request, Depends, APIRouter
from .schema import RegisterRequest,LoginRequest,FavouriteMovieRequest
from .controller import UserController,LoginController,SearchController,FavouriteMovieController
from sqlalchemy.orm import Session
from core.database.session import get_db
from .token import auth_required
from .token import User
move_router = APIRouter()
app = FastAPI()

@move_router.post('/register')
def register(request:Request,dto: RegisterRequest,db: Session = Depends(get_db)):
    lang = request.headers.get('Accept-Language')
    logger.info(lang)
    data = UserController().create_user(dto, db)
    return data

@move_router.post('/login')
def login(request:Request,dto: LoginRequest,db: Session = Depends(get_db)):
    lang = request.headers.get('Accept-Language')
    logger.info(lang)
    data = LoginController().create_token(dto, db)
    return data

@move_router.get('/search')
@auth_required
def search(q: str,request:Request,db: Session = Depends(get_db), page: int = 1,user=User):
    lang = request.headers.get('Accept-Language')
    logger.info(lang)
    out = SearchController().search_movies(q,page,db,user)
    return out

@move_router.post('/me/favourite')
@auth_required
def favourite(request: Request,dto:FavouriteMovieRequest ,db: Session = Depends(get_db),user=User):
    lang = request.headers.get('Accept-Language')
    logger.info(lang)
    out = FavouriteMovieController().add_favourite(db,dto,user)
    return out
    