from functools import wraps
from http.client import HTTPException

from fastapi.responses import JSONResponse
from fastapi import Request, status
import logging

import jwt
from datetime import datetime,timedelta


jwt_secret = '12345678'
jwt_algorithm = 'HS256'


def encode(payload):
    issued_time = datetime.utcnow()
    expired_time = issued_time+timedelta(minutes=15)
    payload['iat'] = issued_time
    payload['exp'] = expired_time
    encoded_string = jwt.encode(payload, jwt_secret, algorithm=jwt_algorithm)
    return encoded_string



def decode(encoded_string):
    decoded_payload = jwt.decode(jwt=encoded_string, key=jwt_secret, algorithms=[jwt_algorithm])
    return decoded_payload

class User:
    id: int
    fullname: str
    email: str


def auth_required(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        try:
            request = kwargs.get("request")
            token  = request.headers.get('Authorization')
            print(token)
            if not token:
                raise Exception("Token not provided")

            token_payload = decode(token)

            if not token_payload:
                raise Exception("Failed to generate payload from token")

        except Exception as e:
            logging.error(str(e))
            return JSONResponse(status_code=status.HTTP_403_FORBIDDEN,
                                content={'details': 'You are not authorized to perform this request.'})
        user  = User()
        user.id = token_payload['id']
        user.fullname = token_payload['fullname']
        user.email = token_payload['email']
        kwargs['user'] = user
        return  func(*args, **kwargs)

    return wrapper