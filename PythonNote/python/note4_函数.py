"""
(一)函数:

你可以定义一个由自己想要功能的函数，以下是简单的规则：
函数代码块以 def 关键词开头，后接函数标识符名称和圆括号 ()。
任何传入参数和自变量必须放在圆括号中间，圆括号之间可以用于定义参数。
函数的第一行语句可以选择性地使用文档字符串—用于存放函数说明。
函数内容以冒号起始，并且缩进。
return [表达式] 结束函数，选择性地返回一个值给调用方。不带表达式的return相当于返回 None。

函数表达式：
def 函数名（参数列表）:
    函数体



(二)参数传递:

在 python 中，类型(string)属于对象("Runoob")，变量(a)是没有类型的：
a=[1,2,3]
a="Runoob"
以上代码中，[1,2,3] 是 List 类型，"Runoob" 是 String 类型，
而变量 a 是没有类型，她仅仅是一个对象的引用（一个指针(指向某个地址的值)），
可以是 List 类型对象，也可以指向 String 类型对象。

在 python 中，strings, tuples, 和 abers 是不可更改的对象，而 list,dict 等则是可以修改的对象。
不可变类型：变量赋值 a=5 后再赋值 a=10，
这里实际是新生成一个 int 值对象 10，再让 a 指向它，而 5 被丢弃，不是改变a的值，相当于新生成了a。
可变类型：变量赋值 list=[1,2,3,4] 后再赋值 list[2]=5 
则是将 list la 的第三个元素值更改，本身la没有动，只是其内部的一部分值被修改了。

python 函数的参数传递：
不可变类型：类似 c++ 的值传递，如 整数、字符串、元组。如fun（a），传递的只是a的值，没有影响a对象本身。
比如在 fun（a）内部修改 a 的值，只是修改另一个复制的对象，不会影响 a 本身。
可变类型：类似 c++ 的引用传递，如 列表，字典。
如 fun（la），则是将 la 真正的传过去，修改后fun外部的la也会受影响
eg.
def immutable(a):
    a += 1
    return 5

a = 3
b = immutable(a)
print(a)

def mutable(a):
    a[2] += 1
    return 5

list1 = [1,2,3,4,5]
list2 =mutable(list1)

print(list1)

(三)参数：

以下是调用函数时可使用的正式参数类型：
1.必需参数
def f(x):
    ……
a = f(1)

2.默认参数
def f(x,y = 8)
    ……
a = f(x = 1, y = 2)         #如果不声明y的值，则y取默认值8
注：默认参数必须放在最后面，否则会报错
注:定义默认参数要牢记一点：默认参数必须指向不变对象！

def add_end(L=[]):
    L.append('END')
    return L
>>> add_end()
['END']
>>> add_end()
['END', 'END']

Python函数在定义的时候，默认参数L的值就被计算出来了，即[]，
因为默认参数L也是一个变量，它指向对象[]，每次调用该函数，如果改变了L的内容，
则下次调用时，默认参数的内容就变了，不再是函数定义时的[]了。


不定长参数

3.可变参数：
可变参数允许你传入0个或任意个参数，
这些可变参数在函数调用时自动组装为一个tuple。

你可能需要一个函数能处理比当初声明时更多的参数。这些参数叫做不定长参数，和上述2种参数不同，声明时不会命名。基本语法如下：
def functionname([formal_args,] *args ):
   function_suite
   return [expression]
加了星号（*）的变量名会存放所有未命名的变量参数。
如果在函数调用时没有指定参数，它就是一个空元组。我们也可以不向函数传递未命名的变量。如下实例：
def printinfo( arg1, *args ):
    "打印任何传入的参数"
    print ("输出: ")
    print (arg1)
    for var in args:
        print (var)
    return;

printinfo( 1 )
>>1
printinfo(1, 2, 3)
>>1
>>2
>>3

n = [1,2,3]
printinfo(*n)      
#Python允许你在list或tuple前面加一个*号，把list或tuple的元素变成可变参数传进去


4.关键字参数
关键字参数允许你传入0个或任意个含参数名的参数，
这些关键字参数在函数内部自动组装为一个dict。

>>> def func(country,province,**kw):
...     print(country,province,kw)
... 
>>> func("China","Sichuan",city = "Chengdu", section = "JingJiang")
China Sichuan {'city': 'Chengdu', 'section': 'JingJiang'}

>>>dict = {'city': 'Chengdu', 'section': 'JingJiang'}
>>>func("China","Sichuan",**dict)
China Sichuan {'city': 'Chengdu', 'section': 'JingJiang'}
#Python允许你在dict前面加**号，把dict的元素变成关键字参数传进去
命名关键字参数必须传入参数名，这和位置参数不同。如果没有传入参数名，调用将报错

5.命名关键字参数
如果要限制关键字参数的名字，就可以用命名关键字参数，
例如，只接收city和job作为关键字参数。这种方式定义的函数如下：
def person(name, age, *, city, job):
# *后面的参数被视为命名关键字参数,这样的关键字参数强制需要输入(但可设默认值)

如果函数定义中已经有了一个可变参数，后面跟着的命名关键字参数就不再需要一个特殊分隔符*了：
def person(name, age, *args, city, job):

#其实命名关键字很像必须参数,只是一定需要直呼其名来传入参数

4.综上
>>> def instance(a,b=1,*c,d,**e):
...     print(a,b,c,d,e)
# a - 必须, b - 默认, c - 可变, d - 命名关键字, e - 关键字     

#暴力传入参数
>>> tuple0 = (1,2,3)
>>> dict0 = {'d':4,'e':5}
>>> instance(*tuple0,**dict0)
1 2 (3,) 4 {'e': 5}
#对于任意函数，都可以通过类似func(*args, **kw)的形式调用它，无论它的参数是如何定义的

#使用*args和**kw是Python的习惯写法，当然也可以用其他参数名，但最好使用习惯用法。



(四)匿名函数：

python 使用 lambda 来创建匿名函数。
所谓匿名，意即没有名字,即用即抛
lambda 只是一个表达式，函数体比 def 简单很多。
lambda的主体是一个表达式，而不是一个代码块。仅仅能在lambda表达式中封装有限的逻辑进去。
lambda 函数拥有自己的命名空间，且不能访问自己参数列表之外或全局命名空间里的参数。
虽然lambda函数看起来只能写一行，却不等同于C或C++的内联函数，后者的目的是调用小函数时不占用栈内存从而增加运行效率。

lambda 函数的语法只包含一个语句，如下：
lambda [arg1 [,arg2,..argn]]:expression

eg.
sum = lambda a, b: a + b


(五)变量作用域

Python 中，程序的变量并不是在哪个位置都可以访问的，访问权限决定于这个变量是在哪里赋值的。
变量的作用域决定了在哪一部分程序可以访问哪个特定的变量名称。Python的作用域一共有4种，分别是：
L （Local） 局部作用域
E （Enclosing） 闭包函数外的函数中
G （Global） 全局作用域
B （Built-in） 内建作用域(内建指的就是python自身)
以 L –> E –> G –>B 的规则查找，
即：在局部找不到，便会去局部外的局部找（例如闭包），再找不到就会去全局找，再者去内建中找。

x = int(2.9)  # 内建作用域
g_count = 0  # 全局作用域
def f():
    o_count = 1  # 闭包函数外的函数中
    def g():
        i_count = 2  # 局部作用域



Python 中只有模块（module），类（class）以及函数（def、lambda）才会引入新的作用域，
其它的代码块（如 if/elif/else/、try/except、for/while等）是不会引入新的作用域的，
也就是说这这些语句内定义的变量，外部也可以访问，如下代码：
if True:
    a = 'I am from Runoob'
print(a)
>>'I am from Runoob'
实例中 a 变量定义在 if 语句块中，但外部还是可以访问的
如果将 a 定义在函数中，则它就是局部变量，外部不能访问:
def f():
    a = 'I am from Runoob'
print(a)
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
NameError: name 'a' is not defined
从报错的信息上看，说明了 a 未定义，无法使用，因为它是局部变量，只有在函数内可以使用。

#怎么理解这个引入新的作用域的喵？？？
简单来说，就是
当你创建一个循环结构的时候，并没有产生一个局部作用域G，大家都还是全局作用域G，可以互相访问
当你定义一个函数的时候，在函数的语句中产生了一个局部作用域G，这个局部作用域G里可以访问域外(def外)的变量,
但域外(def外)则无法访问域内的变量

假设你又定义了一个函数的话，这个函数的语句中也产生了一个局部作用域，
那么G1局部作用域里和G2局部作用域里不能互相访问彼此的变量,域外也无法访问这两个域内的变量

闭包函数外的函数中E指的大概就是循环定义下，相对外层的函数

内建作用域B主要指Python自带的函数,函数也是一种可以访问的东西(变量)嘛(好像不对？？？看最下面)

(六)局部变量和全局变量：
#上面白理解了一大堆……原来下面就有说……不过看起来上面推测对了耶

全局变量和局部变量
定义在函数内部的变量拥有一个局部作用域，定义在函数外的拥有全局作用域。
局部变量只能在其被声明的函数内部访问，而全局变量可以在整个程序范围内访问。
调用函数时，所有在函数内声明的变量名称都将被加入到作用域中。

(七)global 和 nonlocal关键字

当内部作用域想修改外部作用域(G)的变量时，就要用到global和nonlocal关键字了。
#在内部作用域可以访问外部作用域的值(print)，但不能对它进行修改除非用global 或 nonlocal
以下实例修改全局变量 a：

a = 1
def fun1():
    global a  # 需要使用 global 关键字声明
    print(a) 
    a = 2
fun1()
>>1
print(a)
>>2

#list貌似会突破作用域，如果a = []的话，就不需要global都可以引用a了

如果要修改嵌套作用域(E)（enclosing 作用域，外层非全局作用域）中的变量则需要 nonlocal 关键字了，如下实例：
#!/usr/bin/python3
 
def f():
    a = 10
    def g():
        nonlocal a   # nonlocal关键字声明
        a = 100
        print(a)
    g()
    print(a)
f()

有一种需要理解的情况：
a = 10
def f():
    a = a + 1
    print(a)
f()
>>报错,这里同时动用了修改+引用,引用ok,但修改是非法的
而下面这个就没问题
a = 10
def f():
    b = a + 1
    print(b)
f()
>>11




注：关于作用域的一个解释！

对于变量作用域，变量的访问以 L（Local） –> E（Enclosing） –> G（Global） –>B（Built-in） 的规则查找
，即：在局部找不到，便会去局部外的局部找（例如闭包），再找不到就会去全局找，再者去内建中找。
观察以下几个例子，均从内部函数输出变量 x：
1. 局部作用域
x = int(3.3)
x = 0
def outer():
    x = 1
    def inner():
        x = 2
        print(x)
    inner()
outer()
执行结果为 2，因为此时直接在函数 inner 内部找到了变量 x。

2.闭包函数外的函数中
x = int(3.3)
x = 0
def outer():
    x = 1
    def inner():
        i = 2
        print(x)
    inner()
outer()
执行结果为 1，因为在内部函数 inner 中找不到变量 x，继续去局部外的局部——函数 outer 中找，
这时找到了，输出 1。

3.全局作用域
x = int(3.3)
x = 0
def outer():
    o = 1
    def inner():
        i = 2
        print(x)
    inner()
outer()
执行结果为 0，在局部（inner函数）、局部的局部（outer函数）都没找到变量 x，于是访问全局变量，
此时找到了并输出。

4. 内建作用域
x = int(3.3)        #(为什么，这是个内建作用域？是指这一行？还是指x？还是指int()？)
g = 0
def outer():
    o = 1
    def inner():
        i = 2
        print(x)
    inner()
outer()
执行结果为 3，在局部（inner函数）、局部的局部（outer函数）以及全局变量中都没有找到变量x，于是访问内建变量，
此时找到了并输出。
#可否这样理解，这个例子说的有问题,比如说下面这段代码
x = 0
def f():
    def g():
        global x
        x = True
f()
print(x)
#这个x = True时要找变量True的值，局部L找不到找闭包函数外的函数E,再找全局G都找不到了，一翻内建B，哦有Ture，过了
#所以绝大多数情况下，完全不用考虑内建域的问题，毕竟Python不会允许你把True当成变量名来赋值而抢了它的内建域的变量……


内建作用域，例子说的有点问题。在这里纠正一下。
内置作用域是通过一个名为builtin的标准模块来实现的，
但是这个变量名自身并没有放入内置作用域内，所以必须导入这个文件才能够使用它。
在Python3.0中，可以使用以下的代码来查看到底预定义了哪些变量

要在互交模式下输入
>>>import builtins
>>>dir(builtins)

结果为：
['ArithmeticError', 'AssertionError', 'AttributeError', 'BaseException', 'BlockingIOError', 
'BrokenPipeError', 'BufferError', 'BytesWarning', 'ChildProcessError', 'ConnectionAbortedError',
'ConnectionError', 'ConnectionRefusedError', 'ConnectionResetError', 'DeprecationWarning',
'EOFError', 'Ellipsis', 'EnvironmentError', 'Exception', 'False', 'FileExistsError', 
'FileNotFoundError', 'FloatingPointError', 'FutureWarning', 'GeneratorExit', 'IOError',
'ImportError', 'ImportWarning', 'IndentationError', 'IndexError', 'InterruptedError',
'IsADirectoryError', 'KeyError', 'KeyboardInterrupt', 'LookupError', 'MemoryError',
'ModuleNotFoundError', 'NameError', 'None', 'NotADirectoryError', 'NotImplemented', 
'NotImplementedError', 'OSError', 'OverflowError', 'PendingDeprecationWarning',
'PermissionError', 'ProcessLookupError', 'RecursionError', 'ReferenceError', 
'ResourceWarning', 'RuntimeError', 'RuntimeWarning', 'StopAsyncIteration', 'StopIteration', 
'SyntaxError', 'SyntaxWarning', 'SystemError', 'SystemExit', 'TabError', 'TimeoutError',
'True', 'TypeError', 'UnboundLocalError', 'UnicodeDecodeError', 'UnicodeEncodeError',
'UnicodeError', 'UnicodeTranslateError', 'UnicodeWarning', 'UserWarning', 'ValueError', 
'Warning', 'WindowsError', 'ZeroDivisionError', '__build_class__', '__debug__', '__doc__',
'__import__', '__loader__', '__name__', '__package__', '__spec__', 'abs', 'all',
'any', 'ascii', 'bin', 'bool', 'bytearray', 'bytes', 'callable', 'chr', 'classmethod',
'compile', 'complex', 'copyright', 'credits', 'delattr', 'dict', 'dir', 'divmod', 
'enumerate', 'eval', 'exec', 'exit', 'filter', 'float', 'format', 'frozenset',
'getattr', 'globals', 'hasattr', 'hash', 'help', 'hex', 'id', 'input', 'int',
'isinstance', 'issubclass', 'iter', 'len', 'license', 'list', 'locals', 'map', 
'max', 'memoryview', 'min', 'next', 'object', 'oct', 'open', 'ord', 'pow', 
'print', 'property', 'quit', 'range', 'repr', 'reversed', 'round', 'set', 'setattr', 
'slice', 'sorted', 'staticmethod', 'str', 'sum', 'super', 'tuple', 'type', 'vars', 'zip']

"""