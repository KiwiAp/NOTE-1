元类
https://www.liaoxuefeng.com/wiki/0014316089557264a6b348958f449949df42a6d3a2e542c000/0014319106919344c4ef8b1e04c48778bb45796e0335839000
http://www.cnblogs.com/wupeiqi/p/4766801.html
https://www.cnblogs.com/smallmars/p/7058459.html

type()
我们说class的定义是运行时动态创建的，而创建class的方法就是使用type()函数。

type()函数既可以返回一个对象的类型，又可以创建出新的类型，
比如，我们可以通过type()函数创建出Hello类，而无需通过class Hello(object)...的定义：

>>> def fn(self, name='world'): # 先定义函数
...     print('Hello, %s.' % name)
...
>>> Hello = type('Hello', (object,), dict(hello=fn)) # 创建Hello class

要创建一个class对象，type()函数依次传入3个参数：

1.class的名称；
2.继承的父类集合，注意Python支持多重继承，如果只有一个父类，别忘了tuple的单元素写法；
3.class的方法名称与函数绑定，这里我们把函数fn绑定到方法名hello上。
通过type()函数创建的类和直接写class是完全一样的，
因为Python解释器遇到class定义时，
仅仅是扫描一下class定义的语法，然后调用type()函数创建出class。

正常情况下，我们都用class Xxx...来定义类，
但是，type()函数也允许我们动态创建出类来，
也就是说，动态语言本身支持运行期动态创建类，这和静态语言有非常大的不同，

要在静态语言运行期创建类，必须构造源代码字符串再调用编译器，或者借助一些工具生成字节码实现，
本质上都是动态编译，会非常复杂。


metaclass
de = eval('5')

class ListMetaclass(type):  #1
    def __new__(cls,name,bases,attr):  #2
        def add(self, value):   #7
            self.append(value)  
        attr['add'] = add  #8
        return type.__new__(cls,name,bases,attr)   #9

#返回的值:
# cls: <class '__main__.ListMetaclass'>
# name: 'Mylist'
# bases: (<type>,)
# attrs: {'__module__': '__main__', '__qualname__': 'Mylist', 'add': <function ListMetacl...81176CD08>}

'''
__new__
1.当前准备创建的类的对象；

2.类的名字；

3.类继承的父类集合；

4.类的方法集合。

当我们传入关键字参数metaclass时，魔术就生效了，
它指示Python解释器在创建MyList时，要通过ListMetaclass.__new__()来创建，
在此，我们可以修改类的定义，比如，加上新的方法，然后，返回修改后的定义。
'''

class Mylist(list,metaclass = ListMetaclass):   #3
    value = 5    #4
    test = 4    #5
    def sub(self):  #6
        print(self.value)

a = Mylist()
a.add(1)
print(a)

'''
###
1.
class Mylist(list):
    ...
这段代码，其实本质上是在由元类type创建
class Mylist(list,metaclass = type):
    ...
2.
而type的代码内部有:
    def __new__(cls,name,bases,attr):
        ...
        return ...
在metacalss = type时,这段代码(type.__new__)将会被调用,参数被传过去,最后返回一个类
3.
而两段代码的执行顺序是
class type(object):         #1
    def __new__(cls,name,bases,attr)    #2
        ...     #5
        return ...      #6

class Mylist(list,metaclass = type):    #3
    ...     #4
因为程序要扫完Mylist的主体部分(#4),获得完整的attr后再调用__new__生成类
4.
在我们自己定义的metaclass中,我们拥有自己的__new__,
在这个__new__方法中对输入进来的参数attr进行修改,
最后再交给type.__new__来生成类

一个实例:
'''
' Simple ORM using metaclass '
debug = eval('5')

class ModelMetaclass(type):

    def __new__(cls, name, bases, attrs):
        if name=='Model':
            return type.__new__(cls, name, bases, attrs)
        print('Found model: %s' % name)
        mappings = dict()
        for k, v in attrs.items():
            if isinstance(v, Field):
                print('Found mapping: %s ==> %s' % (k, v))
                mappings[k] = v
        for k in mappings.keys():
            attrs.pop(k)
        attrs['__mappings__'] = mappings # 保存属性和列的映射关系
        attrs['__table__'] = name # 假设表名和类名一致
        return type.__new__(cls, name, bases, attrs)

class Model(dict, metaclass=ModelMetaclass):

    def __init__(self, **kw):
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
        for k, v in self.__mappings__.items():
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


# testing code:

class User(Model):
    id = IntegerField('id')
    name = StringField('username')
    email = StringField('email')
    password = StringField('password')

u = User(id=12345, name='Michael', email='test@orm.org', password='my-pwd')
u.save()

'''
Found model: User
Found mapping: id ==> <IntegerField:id>
Found mapping: name ==> <StringField:username>
Found mapping: email ==> <StringField:email>
Found mapping: password ==> <StringField:password>
SQL: insert into User (id,username,email,password) values (?,?,?,?)
ARGS: [12345, 'Michael', 'test@orm.org', 'my-pwd']
'''


一个实用的的骚写法:
class Type(type):
    def __repr__(cls):
        return cls.__name__

class O(object, metaclass=Type): pass

class A(O): pass

class B(O): pass

class C(O): pass

class D(O): pass

class E(O): pass

class K1(A, B, C): pass

class K2(D, B, E): pass

class K3(D, A): pass

class Z(K1, K2, K3): pass

print(Z.mro())