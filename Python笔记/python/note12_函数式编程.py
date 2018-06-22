1.高阶函数
1.1
>>> abs(-10)
10
>>> abs
<built-in function abs>

1.2
>>> f = abs
>>> f
<built-in function abs>
>>> f(-10)
10
#变量f现在已经指向了abs函数本身。直接调用abs()函数和调用变量f()完全相同。

1.3
>>> abs = 10
>>> abs
10
函数名其实就是指向函数的变量！
对于abs()这个函数，完全可以把函数名abs看成变量
它指向一个可以计算绝对值的函数

#要恢复abs函数，请重启Python交互环境

#由于abs函数实际上是定义在import builtins模块中的，
# 所以要让修改abs变量的指向在其它模块也生效，
# 要用import builtins; builtins.abs = 10

1.4 高阶函数
既然变量可以指向函数，函数的参数能接收变量，
那么一个函数就可以接收另一个函数作为参数，这种函数就称之为高阶函数
def add(x, y, f):
    return f(x) + f(y)
x = -5
y = 6
f = abs
print(add(x,y,f))

把函数作为参数传入，这样的函数称为高阶函数，
函数式编程就是指这种高度抽象的编程范式


2.map()函数 和reduce()函数
2.1
map()函数接收两个参数，一个是函数，一个是Iterable，
map将传入的函数依次作用到序列的每个元素，并把结果作为新的Iterator返回,
可以用list提取出来。

>>> def f(x):
...     return x * x
...
>>> r = map(f, [1, 2, 3, 4, 5, 6, 7, 8, 9])
>>> list(r)
[1, 4, 9, 16, 25, 36, 49, 64, 81]

2.2
reduce()函数接收两个参数，一个是函数，一个是Iterable，
reduce把一个函数作用在一个序列[x1, x2, x3, ...]上，
这个函数必须接收两个参数，reduce把结果继续和序列的下一个元素做累积计算，

返回那个函数最终返回的结果

其效果就是：
reduce(f, [x1, x2, x3, x4]) = f(f(f(x1, x2), x3), x4)

>>> from functools import reduce
>>> def add(x, y):
...     return x + y
...
>>> reduce(add, [1, 3, 5, 7, 9])
25

2.3例:
2.3.1
但是如果要把序列[1, 3, 5, 7, 9]变换成整数13579，reduce就可以派上用场：

>>> from functools import reduce
>>> def fn(x, y):
...     return x * 10 + y
...
>>> reduce(fn, [1, 3, 5, 7, 9])
13579

2.3.2
这个例子本身没多大用处，但是，如果考虑到字符串str也是一个序列，
对上面的例子稍加改动，配合map()，我们就可以写出把str转换为int的函数：
>>> from functools import reduce
>>> def fn(x, y):
...     return x * 10 + y
...
>>> def char2num(s):
...     digits = {'0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9}
...     return digits[s]
...
>>> reduce(fn, map(char2num, '13579'))
13579

2.3.3
还可以用lambda函数进一步简化成：

from functools import reduce

DIGITS = {'0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9}

def char2num(s):
    return DIGITS[s]

def str2int(s):
    return reduce(lambda x, y: x * 10 + y, map(char2num, s))
假设Python没有提供int()函数，你完全可以自己写一个把字符串转化为整数的函数，
而且只需要几行代码

3.filter函数
3.1
Python内建的filter()函数用于过滤序列

和map()类似，filter()也接收一个函数和一个序列。
和map()不同的是，filter()把传入的函数依次作用于每个元素，
然后根据返回值是True还是False决定保留还是丢弃该元素。

返回一个iterator,可以用list提取出来

iterator2 = filter(func,iterator)
#这个filter是怎么运作的呢？首先,它是一个iterator,不当场计算完结果
#每次要next到它的时候,它对它的iterator请求一个next,然后得到的值导进func里,
# 如果返回值是False的话,它就继续对它的iterator请求一个next,继续得到的值加进它的func里,
# 如果返回值是Ture的话,它就把这个得到的值吐出来

#filter可以构成一条长长的iterator链,下层的filter指向上层的filter,顶层的filter指向一个终点iterator作为结束
# 然后底层filter有next请求的时候,把next请求不断往上层发,在终点iterator得到值以后不断往下传,进行每一层的func检验
# 详情请见3.4

相当于:
def filter(func,iterator)：
    while True:
        value = next(iterator)
        if func(value) == True：
            yield value

3.2
例如，在一个list中，删掉偶数，只保留奇数，可以这么写：

def is_odd(n):
    return n % 2 == 1

list(filter(is_odd, [1, 2, 4, 5, 6, 9, 10, 15]))

3.3
注意这种写法:
def it():
    while True:
        ...
        yield ...

iterator = it()
iterator = filter(func,iterator)

print(next(iterator)）
...

这种写法是可以的,因为iterator作为一个变量,始终不过是一个指针
在filter语句中把it()这个真实的iterator传递给filter,
然后自己重新指向filter这个新的iterator

3.4
来一个恐怖的多层iterator : 埃氏筛法
def _odd_iter():
    n = 1
    while True:
        n = n + 2
        yield n

def _not_divisible(n):  #第一次引用这个函数的时候它是_not_divisible,第一次使用这个函数的时候它是lambda ...
    print('currect n is ',n)
    return lambda x: x % n > 0

def primes():
    yield 2
    it = _odd_iter() # 初始序列
    while True:
        n = next(it) # 返回序列的第一个数
        yield n
        it = filter(_not_divisible(n), it) # 构造新序列 
                    #_not_divisible(n)是为了创建一个有着锁死的n的lambda x: x % n > 0,否则每层的lambda里的n会随着primes()域里的n变动而变动

# 打印1000以内的素数:
for n in primes():
    if n < 1000:
        print(n)
    else:
        break
得益于行180,这个段代码会不断生成一层层filter_iterator(lambda ...,filter_iterator(lambda ...,_odd_iter()))
每一个filter_iterator都指向上一层filter_iterator,
当一个filter_iterator被请求一个next的时候,它会一层层往上请求next,直到请求到_odd_iter()为止,
然后这个_odd_iter()吐出来的数被一层层的lambda检验,不断通过并传到下一层,或者不通过则该层的filter_iterator重新向上一层请求next

但很奇怪的是,这样做却不会堆栈溢出,
因为每个filter_iterator仅仅是在占用一点点内存而已,构成的是一个长长的链结构

这样写虽然复杂而难以理解,但算法复杂度(O(n))却很低,计算10000以内的素数只要0.13s
而下面这种常规写法虽然很简单,但算法复杂度(O(n**2))却很高,计算10000一内的素数要5.99s

for i in range(3,1000):
    check = True
    for j in range(2,i):
        if i%j == 0:
            check = False
    if check == True:
        print(i)

4.sorted函数
4.1
sorted()函数也是一个高阶函数，
它还可以接收一个key函数来实现自定义的排序，例如按绝对值大小排序
>>> sorted([36, 5, -12, 9, -21], key=abs)
[5, 9, -12, -21, 36]

4.2
key指定的函数将作用于list的每一个元素上，并根据key函数返回的结果进行排序。
对比原始的list和经过key=abs处理过的list：
list = [36, 5, -12, 9, -21]
keys = [36, 5,  12, 9,  21]

4.3
我们给sorted传入key函数，即可实现忽略大小写的排序：
>>> sorted(['bob', 'about', 'Zoo', 'Credit'], key=str.lower)
['about', 'bob', 'Credit', 'Zoo']

4.4
要进行反向排序，不必改动key函数，可以传入第三个参数reverse=True：
>>> sorted(['bob', 'about', 'Zoo', 'Credit'], key=str.lower, reverse=True)
['Zoo', 'Credit', 'bob', 'about']

5.函数作为返回值
5.1
高阶函数除了可以接受函数作为参数外，还可以把函数作为结果值返回。
我们来实现一个可变参数的求和。通常情况下，求和的函数是这样定义的：
def calc_sum(*args):
    ax = 0
    for n in args:
        ax = ax + n
    return ax

但是，如果不需要立刻求和，而是在后面的代码中，根据需要再计算怎么办？
可以不返回求和的结果，而是返回求和的函数：
def lazy_sum(*args):
    def sum():
        ax = 0
        for n in args:
            ax = ax + n
        return ax
    return sum

当我们调用lazy_sum()时，返回的并不是求和结果，而是求和函数：
>>> f = lazy_sum(1, 3, 5, 7, 9)
>>> f
<function lazy_sum.<locals>.sum at 0x101c6ed90>
>>> f()
25

请再注意一点，当我们调用lazy_sum()时，每次调用都会返回一个新的函数，
即使传入相同的参数：
>>> f1 = lazy_sum(1, 3, 5, 7, 9)
>>> f2 = lazy_sum(1, 3, 5, 7, 9)
>>> f1==f2
False

重点：
在这个例子中，我们在函数lazy_sum中又定义了函数sum
并且，内部函数sum可以引用外部函数lazy_sum的参数和局部变量
当lazy_sum返回函数sum时，相关参数和变量都保存在返回的函数中
这种称为“闭包（Closure）”的程序结构拥有极大的威力

5.2 错误的闭包
def count():
    fs = []
    for i in range(1, 4):
        def f():
            return i*i
        fs.append(f)
    return fs
h1, h2, h3 = count()
print(h1(),h2(),h3())  #-->  9 9 9

#等价代码:
def count():
    i = 1
    def f1():       
        return i*i
    i = 2
    def f2():
        return i*i
    i = 3
    def f3():
        return i*i
    return(f1,f2,f3)
h1,h2,h3 = count()      # h1 = f1, h2 = f2, h3 = f3
print(h1(),h2(),h3())   #当f1调用i时,会往外层函数count里找

返回闭包时牢记一点：返回函数不要引用任何循环变量，或者后续会发生变化的变量。
如果一定要引用循环变量怎么办？
方法是再创建一个函数，用该函数的参数绑定循环变量当前的值，
无论该循环变量后续如何更改，已绑定到函数参数的值不变：

正确的闭包
def count():
    def f(j):
        def g():
            return j*j
        return g
    fs = []
    for i in range(1, 4):
        fs.append(f(i))
    return fs

h1, h2, h3 = count()
print(h1(),h2(),h3())  #-->  1 4 9

#等价代码:
def count():
    def f1(j):
        def g1():
            return j*j
        return g1
    def f2(j):
        def g2():
            return j*j
        return g2
    def f3(j):
        def g3():
            return j*j
        return g3   
    return (f1(1),f2(2),f3(3))

h1, h2, h3 = count()        #h1 = g1, h2 = g2, h3 = g3 
print(h1(),h2(),h3())       #当g1调用j时,会往外层函数f1里找

5.3另一个例子
def createCounter():
    s = [0]
    def counter():
        s[0]+=1
        return s[0]
    return counter

counterA = createCounter()
print(counterA(), counterA(), counterA(), counterA(), counterA())
#1,2,3,4,5
#用list跨闭包传递数据,迭代器一般的骚操作
#同时可以看出,外层函数是不会因为返回了值而就删除的,以防内层函数随时可能的调用

6装饰器
6.1 __name__属性
函数也是对象,函数对象都有个__name__属性,可以拿到函数的名字
>>> def now():
...     print('2015-3-25')
...
>>> f = now
>>> now.__name__
'now'
>>> f.__name__
'now'

6.2装饰器
def now():
    print('2015-3-25')
现在，假设我们要增强now()函数的功能，
比如，在函数调用前后自动打印日志，但又不希望修改now()函数的定义，
这种在代码运行期间动态增加功能的方式，称之为“装饰器”（Decorator）。

def log(func):  #1
    def wrapper(*args, **kw):   #3
        print('call %s():' % func.__name__)     #6
        return func(*args, **kw)    #7
    return wrapper      #4

@log    #2      等效于在每次now()前加一行now = log(now)
def now():  #2 扫@的时候一并扫进去了
    print('2015-3-25')      #8

now()       #5
#--> 
#call now():
#2015-3-25

由于log()是一个decorator，返回一个函数，
所以，原来的now()函数仍然存在，只是[现在同名的now变量指向了新的函数]，
这个新的函数在原来函数的基础上多加了几行,(*args,**kw)用来把参数无损地传过去
于是调用now()将执行新函数:wrapper()函数。

6.3带参数的装饰器
如果decorator本身需要传入参数，那就需要编写一个返回decorator的高阶函数，
比如，要自定义log的文本：

def log(text):
    def decorator(func):
        def wrapper(*args, **kw):
            print('%s %s():' % (text, func.__name__))
            return func(*args, **kw)
        return wrapper
    return decorator

@log('execute')
def now():
    print('2015-3-25')

>>> now()
execute now():
2015-3-25

6.4装饰器对__name__的影响

装饰器也有__name__等属性，
经过decorator装饰之后的函数，因为now指针现在已经指向wrapper函数,
它们的__name__已经从原来的'now'变成了'wrapper'：

>>> now.__name__
'wrapper'

所以，需要把原始函数的__name__等属性复制到wrapper()函数中，
否则，有些依赖函数签名的代码执行就会出错。

一个完整的decorator的写法如下：
import functools

def log(func):
    @functools.wraps(func)      #即在def wrapper的上方再加个@functools.wraps(func)装饰器
    def wrapper(*args, **kw):
        #wrapper.__name__ = func.__name__ , 或这么加也可以
        print('call %s():' % func.__name__)
        return func(*args, **kw)
    return wrapper

6.5一个输出调用函数名和时间的装饰器
import time
def log(func):  
    def wrapper(*args, **kw):   
        wrapper.__name__ = func.__name__
        print('start call : %s()' % func.__name__)     
        a = time.time()
        result = func(*args, **kw)    
        print('end call : %s() , time : %f'%(func.__name__,time.time()-a))
        return result
    return wrapper  

7.偏函数

7.1
偏函数通过设定参数的默认值，可以降低函数调用的麻烦度

假设要转换大量的二进制字符串，每次都传入int(x, base=2)会非常麻烦，
于是，可以定义一个int2()的函数，默认把base=2传进去：

def int2(x, base=2):
    return int(x, base)

functools.partial就是帮助我们创建一个偏函数的，不需要我们自己定义int2()，
可以直接使用下面的代码创建一个新的函数int2：

>>> import functools
>>> int2 = functools.partial(int, base=2)
>>> int2('1000000')
64

functools.partial的作用就是，把一个函数的某些参数给固定住（也就是设置默认值）
返回一个新的函数，而调用这个新函数会更简单
即简化,适用化函数

7.2
偏函数原理:

创建偏函数时，实际上是接收了函数对象、*args和**kw这3个参数

int2 = functools.partial(int, base=2)

int2('10010')
相当于：
kw = { 'base': 2 }
int('10010', **kw)


max2 = functools.partial(max, 10)

max2(5, 6, 7)
相当于:
args = (10, 5, 6, 7)
max(*args)

8.zip函数
zip() 函数用于将任意多个可迭代的对象作为参数，将对象中对应的元素打包成一个个元组，然后返回由这些元组组成的列表。
如果各个迭代器的元素个数不一致，则返回列表长度与最短的对象相同，利用 * 号操作符，可以将元组解压为列表
>>>zipbox = zip([1,2,3],[4,5,6])
>>>print(zipbox)
[(1,4),(2,5),(3,6)]
>>>zip(*zipbox)