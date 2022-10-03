from db_setting import engine


if __name__ == '__main__':
    from models import *
    Base.metadata.create_all(bind=engine)




