'''
https://www.liaoxuefeng.com/wiki/0014316089557264a6b348958f449949df42a6d3a2e542c000/0014318645694388f1f10473d7f416e9291616be8367ab5000
http://www.cnblogs.com/wupeiqi/p/4493506.html
https://www.cnblogs.com/smallmars/p/7058459.html


一、基本语法
1.类的定义
class ClassName():
    ...

2.类的继承
class ClassName(FatherClass1,FatherClass2,...):
    ...

3.类的实例
objectName = ClassName()

4.类的变量,方法

class ClassName():
    classValue = 'this is calssvalue'       #类变量(对象可以访问类变量,但同名的实例变量会覆盖类变量)
    __private_classValue = 'this is private classvalue'     #私有类变量

    def __init__(self):     #this is special method     特殊方法
        self.instanceValue = 'this is instancevalue'        #实例变量(不要将类变量和实例变量赋予相同的名字)
        self.__private_instanceValue = 'this is private instancevalue'      #私有私立变量

    def instanceMethod(self):       #实例方法
        print('this is instanceMethod')
    def __private_instanceMethod(self):     #私有实例方法
        print('this is private instanceMethod')

    @classmethod
    def classMethod(cls):       #类方法
        print('this is classMethod',cls)
    @classmethod
    def __private_classMethod(cls):     #私有类方法
        print('this is private classMethod')        

    def normalMethod():     #普通方法
        print('this is normalMethod')
    def __private_normalMethod():       #私有普通方法
        print('this is private normalMethod') 

class Son(ClassName):
    def __init__(self):
        ClassName.__init__(self)

1.变量/方法的访问途径
访问变量/方法的六种途径：用类访问,用类内方法访问,用对象访问,
用派生类访问,用派生类方法访问,用派生类对象访问

2.非私有/私有变量的区别
非私有变量/方法只要满足了输入的argument,就六种途径都可以访问
私有变量/方法只能用类内方法访问

3.用类/对方访问时,参数的自动传入
用类访问时,如果有'@classmethod'会自动传入参数cls(class的名字或者object的类名)
用对象访问时,会自动传入参数self

4.私有变量的访问
私有变量/方法可以用object/ClassName._ClassName__value/method来访问
因为Python解释器对外把__value变量改成了_ClassNmae__value


二、基本语法二
1.特殊方法

def __init__(self,val1,val2,...):
作用:在创建对象的时候,把参数传递给__init__方法,
其中，self参数在class模块内是必写的,但在创建对象时不用填写

__init__ : 在创建对象时调用
__del__ : 在使用del 释放对象时调用
__str__ : 在使用print()函数时调用
__repr__ : 在使用repr()函数时调用   (偷懒写法__repr__ = __str__)
__call__: 在作为object()函数时调用  (callable检测是否可调用)

__doc__ ： 类的描述信息(在class ClassName():下的''' ... '''部分)
__module__ :  当前操作的对象的模块
__class__ :   当前操作的对象的类
__dict__ : 类或对象中的所有成员
__file__ : 
__package__ :
__anthor__:
__name__:

__setitem__ : 在使用object[]索引赋值时调用
__getitem__(self,n) : 在使用object[]索引调用值时调用
__delitem__ : 在删除object[]索引时调

__iter__ : 在迭代时调用     (判断是否可迭代:from collections import Iterable,isinstance('abc', Iterable))
__next__ : 在迭代时调用

class Fib(object):
    def __init__(self):
        self.a, self.b = 0, 1 # 初始化两个计数器a，b

    def __iter__(self):
        return self # 实例本身就是迭代对象，故返回自己

    def __next__(self):
        self.a, self.b = self.b, self.a + self.b # 计算下一个值
        if self.a > 100000: # 退出循环的条件
            raise StopIteration()
        return self.a # 返回下一个值

__len__ : 在使用len()函数时调用
__cmp__ : 在进行比较<,>,==,!=时调用
__add__: 加运算
__sub__: 减运算
__mul__: 乘运算
__div__: 除运算
__mod__: 求余运算
__pow__: 乘方

__slots__ : 限制绑定
__getattr__ : 动态返回变量/函数/方法(lambda)
__new__ : 
__metaclass__ : 

2.查询函数
type(class/object)      #查询类型
isinstance(object,class/(class1,class2))        #查询类型
issubclass(class,class)         #查询类型
dir(class/object)       #查询变量和方法
help(class)         #查询帮助

三、进阶语法
1.动态语言,鸭子类型
一个对象只要“看起来像鸭子，走起路来像鸭子”，那它就可以被看做是鸭子
只要对象拥有对应的方法,就可以使用不是定义给它的类的函数
不要问我是什么，问我能做什么

2.types 详细检查类型的模块
>>> import types
>>> def fn():
...     pass
...
>>> type(fn)==types.FunctionType
True
>>> type(abs)==types.BuiltinFunctionType
True
>>> type(lambda x: x)==types.LambdaType
True
>>> type((x for x in range(10)))==types.GeneratorType
True

3.dir() 获得一个对象的所有变量和方法

4.
hasattr() 检查对象是否拥有变量/方法
setattr() 给对象设置变量/方法
getattr() 获取对象的变量/方法

5.动态绑定

给对象绑定一个(实例)变量
object.instanvalue = ...

给对象绑定一个方法
def method(self):
    ...
object.method = types.MethodTpye(method,object) 

给类绑定一个方法
def method(self):
    ...
Class.method = method

6.限制绑定
__slots__ = ('valueName1','valueName2',...)     #用tuple定义允许绑定的属性名称
#仅对当前类起作用，对继承的子类不起作用

7.装饰器@property - 创建属性(功能：属性内部进行一系列的逻辑计算，最终将计算结果返回)

    @property   #获取
    def pro_value(self):
        return self._pro_value

    @pro_value.setter   #修改
    def pro_value(self, value):
        self._pro_value = value     #注意不能直接用self.pro_value = value,会无限循环

    @pro_value.deleter    #删除
    def pro_value(self):
        ...

object.pro_value
object.pro_value = 123
del object.pro_value

8.多重继承Mixln

在设计类的继承关系时，通常，主线都是单一继承下来的，例如，Ostrich继承自Bird
但是，如果需要“混入”额外的功能，通过多重继承就可以实现
比如，让Ostrich除了继承自Bird外，再同时继承Runnable。这种设计通常称之为MixIn

MixIn的目的就是给一个类增加多个功能，
在设计类的时候，我们优先考虑通过多重继承来组合多个MixIn的功能，
而不是设计多层次的复杂的继承关系

这样一来，我们不需要复杂而庞大的继承链，只要选择组合不同的类的功能，就可以快速构造出所需的子类

9.__getattr__方法, __setattr__方法

class Student(object):

    def __init__(self):
        self.name = 'Michael'

    def __getattr__(self, attr):
        if attr=='score':
            return 99

>>> s.score
99

#注意，只有在没有找到属性的情况下，才调用__getattr__
# 已有的属性，不会在__getattr__中查找

***
举个例子：

现在很多网站都搞REST API，比如新浪微博、豆瓣啥的，调用API的URL类似：

http://api.server/user/friends
http://api.server/user/timeline/list
如果要写SDK，给每个URL对应的API都写一个方法，那得累死，而且，API一旦改动，SDK也要改。

利用完全动态的__getattr__，我们可以写出一个链式调用：

class Chain(object):

    def __init__(self, path=''):
        self._path = path

    def __getattr__(self, path):
        return Chain('%s/%s' % (self._path, path))

    def __str__(self):
        return self._path

    __repr__ = __str__
试试：

>>> Chain().status.user.timeline.list
'/status/user/timeline/list'
这样，无论API怎么变，SDK都可以根据URL实现完全动态的调用，而且，不随API的增加而改变！
***

10.多继承问题(钻石继承)

A()
B(A) C()
D(B)
D.mro() = [D,B,A,C] - 深度优先

A()
B(A) C(A)
D(B)
D.mro() = [D,B,C,A] - 广度优先(钻石继承)
#实际更复杂,python3用的不是简单的深度优先或者广度优先,而是C3算法

http://python-history.blogspot.hk/2010/06/method-resolution-order.html
https://en.wikipedia.org/wiki/C3_linearization

ClassName.mro() - 查询查找顺序(method resolution order)
super() - 调用父类,详情请见:
https://blog.csdn.net/langb2014/article/details/54800203
http://python.jobbole.com/86787/
#super默认自带两参数:super(cls,self)
#多继承时,super根据mro来决定谁是父类
'''