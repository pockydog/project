from passlib.context import CryptContext
from datetime import datetime, timedelta

import jwt

from config import Config

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")


class Encrypt:
    @staticmethod
    def get_password_hash(password):
        return pwd_context.hash(password)

    @staticmethod
    def verify_password(password, hashed_password):
        return pwd_context.verify(password, hashed_password)


class JWTCoder:
    @staticmethod
    def _get_token(expire_time, salt, **kwargs):
        payload = {
            **kwargs,
            'exp': expire_time
        }
        return jwt.encode(payload=payload, key=salt, algorithm='HS256')

    @classmethod
    def get_access_token(cls, **kwargs):
        time_offset = timedelta(seconds=Config.ACCESS_TOKEN_EXPIRE_TIME)
        expire_time = datetime.utcnow() + time_offset
        return cls._get_token(expire_time=expire_time, salt=Config.SALT, **kwargs)

    @classmethod
    def get_refresh_token(cls, **kwargs):
        time_offset = timedelta(seconds=Config.REFRESH_TOKEN_EXPIRE_TIME)
        expire_time = datetime.utcnow() + time_offset
        return cls._get_token(expire_time=expire_time, salt=Config.SALT, **kwargs)





