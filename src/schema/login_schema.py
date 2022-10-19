from typing import Union, Optional
from pydantic import BaseModel, EmailStr


class UserBasicSchema(BaseModel):
    account: str
    name: Union[str, None] = None
    phone: Union[str, None] = None
    email: Union[EmailStr, None] = None
    contant: Union[str, None] = None
    remark: Union[str, None] = None


class UserRegisterSchema(BaseModel):
    account: str
    password: str


class UserGetInfoSchema(BaseModel):
    id: int


class UserLoginSchema(BaseModel):
    account: str
    password: str

