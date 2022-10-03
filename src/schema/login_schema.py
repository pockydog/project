from typing import Union


class UserBasicSchema:
    def __init__(self,
                 account: str,
                 name: Union[str, None] = None,
                 phone: Union[str, None] = None,
                 email: Union[str, None] = None,
                 contant: Union[str, None] = None,
                 remark: Union[str, None] = None):
        self.name = name
        self.account = account
        self.phone = phone
        self.email = email
        self.contant = contant
        self.remark = remark


class UserRegisterSchema:
    def __init__(self, account: str, password: str):
        self.account = account
        self.password = password


class UserGetInfoSchema:
    def __init__(self, id_: int):
        self.id = id_


class UserLoginSchema:
    def __init__(self, account: str, password: str):
        self.account = account,
        self.password = password

