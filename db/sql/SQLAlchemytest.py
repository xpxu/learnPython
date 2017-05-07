# -*- coding: utf-8 -*-

# 导入:
from sqlalchemy import Column, String, create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.exc import IntegrityError
#from sqlalchemy.schema import ForeignKey
#from sqlalchemy.orm import relationship


# 创建对象的基类:
Base = declarative_base()

class User(Base):
    # 表的名字:
    __tablename__ = 'user'

    # 表的结构:
    id = Column(String(20), primary_key=True)
    name = Column(String(20))



# 初始化数据库连接:
# '数据库类型+数据库驱动名称://用户名:口令@机器地址:端口号/数据库名'
engine = create_engine('mysql+mysqlconnector://root:password@localhost:3306/test')
# 创建DBSession类型:
DBSession = sessionmaker(bind=engine)



'''
add a user in user table 实际就是存储一个user对象
'''
# 创建session对象:
session = DBSession()
# 创建新User对象:
new_user = User(id='1', name='Jim')
# 添加到session:
session.add(new_user)
    # 提交即保存到数据库:
session.commit()

# 关闭session:
session.close()



'''
query user with id 5 in user table 实际就是获取一个user对象
'''
# 创建Session:
session = DBSession()
# 创建Query查询，filter是where条件，最后调用one()返回唯一行，如果调用all()则返回所有行:
user = session.query(User).filter(User.id=='1').one()
# 打印类型和对象的name属性:
print 'type:', type(user)
print 'name:', user.name
print 'id:', user.id
# 关闭Session:
session.close()


