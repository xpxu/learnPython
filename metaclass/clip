# -*- coding:utf-8 -*-

'''
Metaclass在ORM中的作用是为了把field统一存放到__mappings__当中，
便于model模块数据传递的迭代操作。如下：
    def save(self):
        fields = []
        params = []
        args = []
        #use a iterator here with __mappings__. 
        for k, v in self.__mappings__.iteritems():
            fields.append(v.name)
            params.append('?')
            args.append(getattr(self, k, None))
        sql = 'insert into %s (%s) values (%s)' % (self.__table__, ','.join(fields), ','.join(params))
        print('SQL: %s' % sql)
        print('ARGS: %s' % str(args))

'''

import json

class ModelMetaclass(type):
    def __new__(cls, name, bases, attrs):
        '''
	四个参数依次为：
	cls: 当前准备创建的类；
	name: 当前类的名字；
	bases: 当前类继承的父类集合；
	attrs: 当前类的属性集合,不包括其父类的属性。
        '''
        print '__new__ is called'
        if name=='Model':
            print 'first time for Model'
            return type.__new__(cls, name, bases, attrs)
        print 'second time for Field'
        mappings = dict()
        for k, v in attrs.iteritems():
            print k,v
            if isinstance(v, Field):
                print('Found mapping: %s==>%s' % (k, v))
                mappings[k] = v
        for k in mappings.iterkeys():
            attrs.pop(k)
        attrs['__table__'] = name # 假设表名和类名一致
        attrs['__mappings__'] = mappings # 保存属性和列的映射关系
        print 'attrs is %s' % attrs
        print 'name is %s' % name
        print 'bases are %s'  % bases
        return type.__new__(cls, name, bases, attrs)


class Model(dict):
    __metaclass__ = ModelMetaclass

    def __init__(self, **kw):
        print '__init__ is called'
        super(Model, self).__init__(**kw)

    def __getattr__(self, key):
        try:
            return self[key]
        except KeyError:
            raise AttributeError(r"'Model' object has no attribute '%s'" % key)

    def __setattr__(self, key, value):
        self[key] = value

    def save(self):
        fields = []
        params = []
        args = []
        for k, v in self.__mappings__.iteritems():
            fields.append(v.name)
            params.append('?')
            args.append(getattr(self, k, None))
        sql = 'insert into %s (%s) values (%s)' % (self.__table__, ','.join(fields), ','.join(params))
        print('SQL: %s' % sql)
        print('ARGS: %s' % str(args))

class Field(object):
    def __init__(self, name, column_type):
        self.name = name
        self.column_type = column_type
    def __str__(self):
        return '<%s:%s>' % (self.__class__.__name__, self.name)


class StringField(Field):
    def __init__(self, name):
        super(StringField, self).__init__(name, 'varchar(100)')

class IntegerField(Field):
    def __init__(self, name):
        super(IntegerField, self).__init__(name, 'bigint')


class User(Model):
    # 定义类的属性到列的映射：
    id = IntegerField('id')
    name = StringField('username')
    email = StringField('email')
    password = StringField('password')


if __name__  == '__main__':
    user = User(id=12345, name='Michael', email='test@orm.org', password='my-pwd')
    print getattr(user, 'id')
    print dir(user)
    print dir(User)
    with open('user.json','w') as f:
	#json.dump(dict(user), f, indent=4) 
	json.dump(user, f, indent=4)	
