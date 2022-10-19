from models.models import User
from db_setting import session
from utils.encrypt_tool import *


class LoginHandler:

    @classmethod
    def register(cls, account, password):
        cls.validate_user(method=User, account=account)
        user = User(
            account=account,
            password=password,
        )
        if password:
            hash_password = Encrypt.get_password_hash(user.password)
            user.password = hash_password
        session.add(user)
        session.flush()
        result = {
            'id': user.id,
            'name': user.name,
            'account': user.account,
            'password': user.password,
            'phone': user.phone,
            'email': user.email,
            'contant': user.contant,
            'remark': user.remark,
        }
        session.commit()
        return result

    @classmethod
    def add_user(cls, account, name=None, phone=None, email=None, contant=None, remark=None):
        if not account:
            raise Exception('User not exist')
        user = session.query(User).filter(User.account == account).first()
        if not user:
            raise Exception('User not found')
        if name:
            user.name = name
        if phone:
            user.phone = phone
        if email:
            user.email = email
        if contant:
            user.contant = contant
        if remark:
            user.remark = remark
        session.add(user)
        session.flush()
        result = {
            'id': user.id,
            'name': user.name,
            'account': user.account,
            'phone': user.phone,
            'email': user.email,
            'contant': user.contant,
            'remark': user.remark,
        }
        session.commit()
        return result

    @classmethod
    def show_user(cls, id_):
        condition = list()
        result_list = list()
        if id_:
            condition.append(User.id == id_)
        user = session.query(User).filter(*condition).first()
        if not user:
            raise Exception('User Id not found')
        result = {
            'id': user.id,
            'name': user.name,
            'account': user.account,
            'password': user.password,
        }
        result_list.append(result)
        return result_list

    @classmethod
    def validate_user(cls, method, account):
        condition = list()
        if account:
            condition.append(User.account == account)
        validate_phone = session.query(method).filter(*condition).first()
        if validate_phone:
            raise Exception('User already exist')

    @classmethod
    def user_login(cls, account, password):
        user = session.query(User).filter(User.account == account).first()
        if not user:
            raise Exception('Account not exist')
        validate_password = user.password
        check = Encrypt.verify_password(password, validate_password)
        access_token = JWTCoder.get_access_token(
            id=user.id,
        )
        refresh_token = JWTCoder.get_refresh_token(
            id=user.id,
        )
        if check:
            result = {
                'token': access_token,
                'refresh_token': refresh_token,
                'success': True
            }
            return result
        else:
            raise Exception('Password Wrong')
