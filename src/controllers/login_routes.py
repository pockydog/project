from fastapi import APIRouter, Depends

from schema.login_schema import *
from core.login_handler import LoginHandler

user_router = APIRouter(prefix='/user')


@user_router.post('/register')
def user_register(common: UserRegisterSchema = Depends(UserRegisterSchema)):
    """會員註冊"""
    result = LoginHandler.register(
        account=common.account,
        password=common.password,
    )
    return result


@user_router.post('/add-info')
def add_usre(common: UserBasicSchema = Depends(UserBasicSchema)):
    """新增會員資料"""
    result = LoginHandler.add_user(
        name=common.name,
        account=common.account,
        phone=common.phone,
        email=common.email,
        contant=common.contant,
        remark=common.remark
    )
    return result


@user_router.get('/show')
def show_user(common: UserGetInfoSchema = Depends(UserGetInfoSchema)):
    """看會員資料"""
    result = LoginHandler.show_user(
        id_=common.id
    )
    return result


@user_router.post('/login')
def user_login(common: UserLoginSchema = Depends(UserLoginSchema)):
    """登入"""
    result = LoginHandler.user_login(
        account=common.account,
        password=common.password,
    )
    return result
