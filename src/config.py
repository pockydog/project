import os


class Config:
    DB_NAME = os.environ['DB_NAME']
    POSTGRES_USER = os.environ['POSTGRES_USER']
    POSTGRES_PASSWORD = os.environ['POSTGRES_PASSWORD']
    POSTGRES_HOST = os.environ['POSTGRES_HOST']
    POSTGRES_PORT = os.environ['POSTGRES_PORT']
    SQLALCHEMY_BINDS = {
        DB_NAME: f'postgresql://{POSTGRES_USER}:{POSTGRES_PASSWORD}@{POSTGRES_HOST}:{POSTGRES_PORT}/{DB_NAME}'
    }
    SQLALCHEMY_DATABASE_URL = SQLALCHEMY_BINDS[DB_NAME]

    # --- Expire Time --- #
    ACCESS_TOKEN_EXPIRE_TIME = 60 * 60 * 24
    REFRESH_TOKEN_EXPIRE_TIME = 60 * 60 * 24

    # --- Salt --- #
    SALT = os.environ['SALT']
    SECRET_KEY = os.environ.get('SECRET_KEY', None)



