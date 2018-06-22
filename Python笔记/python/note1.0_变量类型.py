"""
(一)对象
1.1 = - 赋值
var1 = 1
a = b = c = 1
a, b, c = 1, 2, "runoob"
a += 1

1.2 del - 删除对象
del var1, var2

1.3 一个变量可以通过赋值指向不同类型的对象。

(二)Number数字:
2.1 数字包含的变量类型有：int、float、bool、complex（复数）
2.2 数值的除法（/）总是返回一个浮点数，要获取整数使用//操作符
2.3 在混合计算时，Python会把整型转换成为浮点数

(三)String字符串:
3.1 Python中的字符串用单引号(')或双引号(")括起来，同时使用反斜杠(\)转义特殊字符。
3.2 字符串可以被索引和截取
3.3 mutable的字符串类型 : bytearray

(四)List列表:
4.1 List是Python中使用最频繁的数据类型。
4.2 列表可以完成大多数集合类的数据结构实现。
列表中元素的类型可以不相同，它支持数字，字符串甚至可以包含列表（所谓嵌套）。
4.3 列表是写在方括号([])之间、用逗号分隔开的元素列表。
4.4 和字符串一样，列表同样可以被索引和截取，列表被截取后返回一个包含所需元素的新列表

(五)Tuple元组:
5.1 元组（tuple）与列表类似，不同之处在于元组的元素不能修改。元组写在小括号(())里，元素之间用逗号隔开
5.2 元组中的元素类型也可以不相同
5.3 元组与字符串类似，可以被索引且下标索引从0开始，-1 为从末尾开始的位置，也可以进行截取
5.4 虽然tuple的元素不可改变，但它可以包含可变的对象，比如list列表
5.5 一般来说，函数的返回值一般为一个。而函数返回多个值的时候，是以元组的方式返回的

string、list和tuple都属于sequence（序列）

(六)Set集合:
6.1 集合（set）是一个无序不重复元素的序列。
6.2 基本功能是进行成员关系测试和删除重复元素。
6.3 可以使用大括号 { } 或者 set() 函数创建集合，
注意:创建一个空集合必须用 set() 而不是 { }，因为 { } 是用来创建一个空字典。

(七)Dictionary字典:
7.1 字典（dictionary）是Python中另一个非常有用的内置数据类型。
7.2 列表是有序的对象结合，字典是无序的对象集合。两者之间的区别在于：字典当中的元素是通过键来存取的，而不是通过偏移存取。
7.3 字典是一种映射类型，字典用"{ }"标识，它是一个无序的键(key) : 值(value)对集合。
7.4 键(key)必须使用不可变类型。
7.5 在同一个字典中，键(key)必须是唯一的。

(八)集合
set(mutable)
frozenset(immutable)

(九)变量类型函数:
type() - 查询变量类型，返回变量类型
isinstance() - 检查变量类型，返回布尔

int(x [,base]) - 将x转换为一个整数,base用于转为几进制,默认base = 10
float(x) - 将x转换到一个浮点数
str(x) - 将对象 x 转换为字符串
eval(str) - 用来计算在字符串中的有效Python表达式,并返回一个对象

complex(real [,imag]) - 创建一个复数
tuple(s) - 将序列 s 转换为一个元组
list(s) - 将序列 s 转换为一个列表             #不要用list命名list!否则会用不了list()
set(s) - 转换为可变集合
dict(d) - 创建一个字典。d 必须是一个序列 (key,value)元组。
frozenset(s) - 转换为不可变集合

repr(x) - 将对象 x 转化为供解释器读取的形式
chr(x) - 将一个整数转换为一个ascii字符          #可以用来作字母和数字的相互映射
ord(x) - 将一个ascii字符转换为它的整数值
hex(x) - 将一个整数转换为一个十六进制字符串
oct(x) - 将一个整数转换为一个八进制字符串
bin(x) - 将一个整数转换为一个二进制字符串

list(str) - 把str拆成list
''.join - 把list合成str

(九)分数:
>>> from fractions import Fraction
>>> Fraction(10, 6) 
Fraction(5, 3) # notice it's been reduced to lowest terms
>>> Fraction(1, 3) + Fraction(2, 3) # 1/3 + 2/3 = 3/3 = 1/1
Fraction(1, 1)
>>> f = Fraction(10, 6)
>>> f.numerator
5
>>> f.denominator
3

(十)小数:
>>> from decimal import Decimal as D # rename for brevity
>>> D(3.14) # pi, from float, so approximation issues
Decimal('3.140000000000000124344978758017532527446746826171875')
>>> D('3.14') # pi, from a string, so no approximation issues
Decimal('3.14')
>>> D(0.1) * D(3) - D(0.3) # from float, we still have the issue
Decimal('2.775557561565156540423631668E-17')
>>> D('0.1') * D(3) - D('0.3') # from string, all perfect
Decimal('0.0')

>>> D('1')/D('3')
Decimal('0.3333333333333333333333333333')
>>> print(D('1')/D('3'))
0.3333333333333333333333333333
>>> decimal.getcontext().prec = 40
>>> print(D('1')/D('3'))
0.3333333333333333333333333333333333333333(精确到40位, 正常是28位)

(十一)collection 模块
官方文档 : https://docs.python.org/3.6/library/collections.html?highlight=collection#module-collections
namedtuple() - -A factory function for creating tuple subclasses with named fields
#可以通过tuple.attribute来取代tuple[0]来索引
deque - A list-like container with fast appends and pops on either end
ChainMap - A dict-like class for creating a single view of multiple mappings
#为一个顶层map(dict)始终保留一组默认键值
Counter - A dict subclass for counting hashable objects
OrderedDict - A dict subclass that remembers the order entries were added
defaultdict - A dict subclass that calls a factory function to supply missing values
#有默认值的dict
UserDict - A wrapper around dictionary objects for easier dict subclassing
UserList - A wrapper around list objects for easier list subclassing
UserString - A wrapper around string objects for easier string subclassing


(十二)enum类型(枚举类型) - 常数

from enum import Enum

Month = Enum('Month', ('Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec'))
for name, number in Month.__members__.items():
    print(name,':',number.value)

value属性则是自动赋给成员的int常量，默认从1开始计数。
如果需要更精确地控制枚举类型，可以从Enum派生出自定义类：

from enum import Enum, unique

@unique
class Weekday(Enum):
    Sun = 0 # Sun的value被设定为0
    Mon = 1
    Tue = 2
    Wed = 3
    Thu = 4
    Fri = 5
    Sat = 6
print(Weekday.Mon)
@unique装饰器可以帮助我们检查保证没有重复值。

