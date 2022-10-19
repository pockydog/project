from sqlalchemy import Boolean, Column, Integer, String, JSON
from sqlalchemy.ext.declarative import declarative_base


Base = declarative_base()


class User(Base):
    __bind__ = 'vicky_db'
    __tablename__ = 'user'
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(64), comment='名稱')
    account = Column(String(64), comment='帳號')
    password = Column(String(128), comment='密碼')
    phone = Column(String(64), comment='手機號碼')
    email = Column(String(300), comment='信箱')
    is_block = Column(Boolean(), default=False, comment='0:啟用, 1:停用')
    contant = Column(JSON(), comment='聯絡方式')
    remark = Column(String(128), comment='備註')
