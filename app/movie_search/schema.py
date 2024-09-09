from pydantic import BaseModel


class RegisterRequest(BaseModel):
    fullname: str
    email: str
    password: str


class RegisterResponse(BaseModel):
    id: int
    fullname: str
    email: str


class LoginRequest(BaseModel):
    email: str
    password: str


class FavouriteMovieRequest(BaseModel):
    imdb_id : str