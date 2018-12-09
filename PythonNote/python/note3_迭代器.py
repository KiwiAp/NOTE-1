"""

迭代器：
迭代是Python最强大的功能之一，是访问集合元素的一种方式
迭代器是一个可以记住遍历的位置的对象
迭代器对象从集合的第一个元素开始访问，直到所有的元素被访问完结束。迭代器只能往前不会后退

为什么要用迭代器呢？据说是因为如果用for in迭代会占用大量的内存，而iter每次只占一点点内存
(大概是这样子！待查证！?)

一种解释：对应下面的斐波拉契数列
一个函数 f，f 返回一个 list，这个 list 是动态计算出来的（不管是数学上的计算还是逻辑上的读取格式化）
并且这个 list 会很大（无论是固定很大还是随着输入参数的增大而增大），

这个时候，我们希望每次调用这个函数并使用迭代器进行循环的时候一个一个的得到每个 list 元素
而不是直接得到一个完整的 list 来节省内存，这个时候 yield 就很有用。


(一) 迭代器 - iter()和next()
1.1 迭代器有两个基本的方法：iter() 和 next()
字符串,列表或元组对象都可用于创建迭代器

eg.
list = [1,2,3,4,5]
it = iter(list)
print(it)
>><list_iterator object at 0x000001C325B8D2E8>
print(next(it))
>>1
print(next(it))
>>2
print(next(it))
>>3

1.2 迭代器对象可以使用常规for语句进行遍历
list = [1,2,3,4,5]
it = iter(list)    # 创建迭代器对象
for i in it:
    print (i)


1.3 一种生成迭代器的方法

>>> l = [i for i in range(0,15)]
>>> print(l)
[0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14]
>>> m = (i for i in range(0,15))
>>> print(m)
<generator object <genexpr> at 0x104b6f258>         #为什么m是迭代器而不是tuple?
>>> print(type(m))
<class 'generator'>
>>> for g in m:
...     print(g,end=', ')
... 
0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14,


(二) 生成器 - yield

2.1
import sys
 
def fibonacci(n): # 生成器函数 - 斐波那契
    a, b, counter = 0, 1, 0
    while True:
        yield a
        a, b = b, a + b
        counter += 1
f = fibonacci(10) # f 是一个迭代器，由生成器返回生成
 
for i in range(10):
    print (next(f))

#可拿去debug研究每一步的过程

或者：
import sys
 
def fibonacci(n): # 生成器函数 - 斐波那契
    a, b, counter = 0, 1, 0
    while counter < n:
        yield a
        a, b = b, a + b
        counter += 1

for i in fibonacci(10):         #提取数据直到生成器不生成数据为止
    print (i)


简单地讲，yield 的作用就是把一个函数变成一个 generator，带有 yield 的函数不再是一个普通函数,
Python 解释器会将其视为一个 generator，调用 fab(5) 不会执行 fab 函数，而是返回一个 iterable 对象.

在 while 循环执行时，每次循环都会执行 while 函数内部的代码，执行到 yield a 时，fab 函数就返回一个迭代值a，
下次迭代时，代码从 yield b 的下一条语句继续执行，
而函数的本地变量看起来和上次中断执行前是完全一样的，于是函数继续执行，直到再次遇到 yield。    


#我的理解是，迭代器就是一个可以不断取数据出来的集合,
#而生成器就是一个迭代器，通过特定的算法，把特定的数据源源不断地吐出来,
# 只是可能迭代器存储的数据是有限的，而生成器能生成的数据是无限的(也可以优先)。?

另一个版本的：
import sys
 
def fibonacci(n): # 生成器函数 - 斐波那契
    a, b, counter = 0, 1, 0
    while True:
        if (counter > n): 
            return
        yield a
        a, b = b, a + b
        counter += 1
f = fibonacci(10) # f 是一个迭代器，由生成器返回生成
 
while True:
    try:
        print (next(f), end=" ")
    except StopIteration:
        sys.exit()


return 的作用：
在一个 generator function 中，如果没有 return，则默认执行至函数完毕，
如果在执行过程中 return，则直接抛出 StopIteration 终止迭代。

2.2
另一个 yield 的例子来源于文件读取。如果直接对文件对象调用 read() 方法，会导致不可预测的内存占用。
好的方法是利用固定长度的缓冲区来不断读取文件内容。
通过 yield，我们不再需要编写读文件的迭代类，就可以轻松实现文件读取：

def read_file(fpath):
    BLOCK_SIZE = 1024
    with open(fpath, 'rb') as f:
        while True:
            block = f.read(BLOCK_SIZE)
            if block:
               yield block
            else:
               return

参考 : http://www.runoob.com/w3cnote/python-yield-used-analysis.html

更好的参考 : https://www.liaoxuefeng.com/wiki/0014316089557264a6b348958f449949df42a6d3a2e542c000/0014317799226173f45ce40636141b6abc8424e12b5fb27000
小结:
凡是可作用于for循环的对象都是Iterable类型；
凡是可作用于next()函数的对象都是Iterator类型，它们表示一个惰性计算的序列；
集合数据类型如list、dict、str等是Iterable但不是Iterator，不过可以通过iter()函数获得一个Iterator对象。
