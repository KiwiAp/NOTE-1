
异常类型：
AttributeError 调用不存在的方法引发的异常
EOFError    遇到文件末尾引发的异常
ImportError 导入模块出错引发的异常
IndexError    列表越界引发的异常
IOError    I/O操作引发的异常，如打开文件出错等
KeyError  使用字典中不存在的关键字引发的异常
NameError 使用不存在的变量名引发的异常
TabError 语句块缩进不正确引发的异常
ValueError 搜索列表中不存在的值引发的异常
ZeroDivisionError   除数为零引发的异常

(一)try语句
try:
    ……
except (Errortype) as (variable):
    ……

执行顺序：
1.首先，执行try子句（在关键字try和关键字except之间的语句）
2.如果没有异常发生，忽略except子句，try子句执行后结束。
3.如果在执行try子句的过程中发生了异常，那么try子句余下的部分将被忽略。如果异常的类型和 except 之后的名称相符，
那么对应的except子句将被执行。最后执行 try 语句之后的代码。
4.如果一个异常没有与任何的except匹配，那么这个异常将会传递给上层的try中。
注：as 定义异常实例(except IOError as e)

一个 try 语句可能包含多个except子句，分别来处理不同的特定的异常。最多只有一个分支会被执行。
一个except子句可以同时处理多个异常，这些异常将被放在一个括号里成为一个元组


try except 语句还有一个可选的else子句，如果使用这个子句，那么必须放在所有的except子句之后。
这个子句将在try子句没有发生任何异常的时候执行
使用 else 子句比把所有的语句都放在 try 子句里面要好，这样可以避免一些意想不到的、而except又没有捕获的异常。
try:
    ……
except:
    ……
else:
    ……


异常处理并不仅仅处理那些直接发生在try子句中的异常，而且还能处理子句中调用的函数（甚至间接调用的函数）里抛出的异常。

(二)抛出异常
Python 使用 raise 语句抛出一个指定的异常
raise 唯一的一个参数指定了要被抛出的异常。它必须是一个异常的实例或者是异常的类（也就是 Exception 的子类）。
>>> raise NameError('HiThere')
Traceback (most recent call last):
  File "<stdin>", line 1, in ?
NameError: HiThere

(三)用户自定义异常

可以通过创建一个新的exception类来拥有自己的异常。异常应该继承自 Exception 类，或者直接继承，或者间接继承

(四)清理异常行为

try 语句还有另外一个可选的子句finally，它定义了无论在任何情况下都会执行的清理行为
try(一定执行):
    ……
except(try有错误):
    ……
else(try无错误):
    ……
finally(一定执行,先于错误抛出):
    ……
如果一个异常在 try 子句里（或者在 except 和 else 子句里）被抛出，
而又没有任何的 except 把它截住，那么这个异常会在 finally 子句执行后再次被抛出

#在except中的raise语句如果不带参数，就会把当前错误原样抛出。

(五)with …… as 语句
有一些任务，可能事先需要设置，事后做清理工作。对于这种场景，Python的with语句提供了一种非常方便的处理方式。
一个很好的例子是文件处理，你需要获取一个文件句柄，从文件中读取数据，然后关闭文件句柄。

with open("/tmp/foo.txt") as file:
    ……

自动open后close,简洁方便

with的基本思想是with所求值的对象必须有一个__enter__()方法，一个__exit__()方法。
紧跟with后面的语句被求值后，返回对象的__enter__()方法被调用，这个方法的返回值将被赋值给as后面的变量。
当with后面的代码块全部被执行完之后，将调用前面返回对象的__exit__()方法。

------------------------------------------------------------------------------------
6.错误的类

Python的错误其实也是class，所有的错误类型都继承自BaseException，
所以在使用except时需要注意的是，它不但捕获该类型的错误，还把其子类也“一网打尽

比如:
try:
    foo()
except ValueError as e:
    print('ValueError')
except UnicodeError as e:
    print('UnicodeError')
第二个except永远也捕获不到UnicodeError，因为UnicodeError是ValueError的子类，如果有，也被第一个except给捕获了。

Python所有的错误都是从BaseException类派生的，常见的错误类型和继承关系看这里：
https://docs.python.org/3/library/exceptions.html#exception-hierarchy

------------------------------------------------------------------------------------
7.多层调用

使用try...except捕获错误还有一个巨大的好处，就是可以跨越多层调用，
比如函数main()调用foo()，foo()调用bar()，结果bar()出错了，这时，只要main()捕获到了，就可以处理

也就是说，不需要在每个可能出错的地方去捕获错误，只要在合适的层次去捕获错误就可以了。
这样一来，就大大减少了写try...except...finally的麻烦。

------------------------------------------------------------------------------------
8.错误记录

如果不捕获错误，自然可以让Python解释器来打印出错误堆栈，但程序也被结束了。
既然我们能捕获错误，就可以把错误堆栈打印出来，然后分析错误原因，同时，让程序继续执行下去。
Python内置的logging模块可以非常容易地记录错误信息：

import logging
def foo(s):
    return 10 / int(s)

def bar(s):
    return foo(s) * 2

def main():
    try:
        bar('0')
    except Exception as e:
        logging.exception(e)

main()
print('END')
同样是出错，但程序打印完错误信息后会继续执行，并正常退出

------------------------------------------------------------------------------------
9.断言

9.1
凡是用print()来辅助查看的地方，都可以用断言（assert）来替代：

def foo(s):
    n = int(s)
    assert n != 0, 'n is zero!'
    return 10 / n

def main():
    foo('0')
assert的意思是，表达式n != 0应该是True，否则，根据程序运行的逻辑，后面的代码肯定会出错。

如果断言失败，assert语句本身就会抛出AssertionError：

Traceback (most recent call last):
  ...
AssertionError: n is zero!

9.2
启动Python解释器时可以用-O参数来关闭assert
$ python -O err.py
关闭后，你可以把所有的assert语句当成pass来看

-------------------------------------------------------------------------------------
10.logging

logging的功能非常强大,详情请见:https://www.cnblogs.com/liujiacai/p/7804848.html

把print()替换为logging是第3种方式，和assert比，logging不会抛出错误，而且可以输出到文件：

import logging

s = '0'
n = int(s)
logging.info('n = %d' % n)
print(10 / n)
logging.info()就可以输出一段文本。运行，发现除了ZeroDivisionError，没有任何信息。怎么回事？

别急，在import logging之后添加一行配置再试试：

import logging
logging.basicConfig(level=logging.INFO)
看到输出了：

$ python err.py
INFO:root:n = 0
Traceback (most recent call last):
  File "err.py", line 8, in <module>
    print(10 / n)
ZeroDivisionError: division by zero
这就是logging的好处，它允许你指定记录信息的级别，有debug，info，warning，error等几个级别，当我们指定level=INFO时，logging.debug就不起作用了。同理，指定level=WARNING后，debug和info就不起作用了。这样一来，你可以放心地输出不同级别的信息，也不用删除，最后统一控制输出哪个级别的信息。

logging的另一个好处是通过简单的配置，一条语句可以同时输出到不同的地方，比如console和文件。

***虽然用IDE调试起来比较方便，但是最后你会发现，logging才是终极武器

----------------------------------------------------------------------------------------
11.单元测试
https://www.liaoxuefeng.com/wiki/0014316089557264a6b348958f449949df42a6d3a2e542c000/00143191629979802b566644aa84656b50cd484ec4a7838000


----------------------------------------------------------------------------------------
12.文档测试
https://www.liaoxuefeng.com/wiki/0014316089557264a6b348958f449949df42a6d3a2e542c000/0014319170285543a4d04751f8846908770660de849f285000