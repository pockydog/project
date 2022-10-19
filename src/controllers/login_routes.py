from fastapi import APIRouter, Depends

from schema.login_schema import *
from core.login_handler import LoginHandler

user_router = APIRouter(prefix='/user')


@user_router.post('/register')
def user_register(payload: UserRegisterSchema):
    """會員註冊"""
    result = LoginHandler.register(
        account=payload.account,
        password=payload.password,
    )
    return result


@user_router.post('/add-info')
def add_usre(payload: UserBasicSchema):
    """新增會員資料"""
    result = LoginHandler.add_user(
        name=payload.name,
        account=payload.account,
        phone=payload.phone,
        email=payload.email,
        contant=payload.contant,
        remark=payload.remark
    )
    return result


@user_router.get('/show')
def show_user(user: UserGetInfoSchema = Depends(UserGetInfoSchema)):
    """查看會員資料"""
    result = LoginHandler.show_user(
        id_=user.id
    )
    return result


@user_router.post('/login')
def user_login(payload: UserLoginSchema):
    """登入"""
    result = LoginHandler.user_login(
        account=payload.account,
        password=payload.password,
    )
    return result

