"""
问：VScode怎么打开互交模式？
问：不知道为什么，我的VScode用调试的话，第一行一定要加含eval()函数的任意语句？

操作技巧：
1.多行缩进: ctrl+[ / ctrl+]
2.操作符(=)两段加入空格使程序更容易阅读
3.查询pydoc: 直接在命令行(win +R cmd或者是power shell)中输入python –m pydoc –b
4.python对大小写敏感，函数不要大写，变量区分大小写
5.条件、循环等结构以缩进来判断结束
6.变量由字母,数字,下划线组成，数字不能作开头
7.常用下划线代替空格

VSCode小技巧:
1.按alt+shift+f自动格式化代码(装了yapf后)
2.Ctrl+鼠标左键点击函数名或者类名即可跳转到定义处，在函数名或者类名上按F12也可以实现同样功能

用& python filename来在cmd中打开python文件

学习网站：
菜鸟编程:
http://www.runoob.com/python3/python3-tutorial.html
Crossin的编程教室:
http://crossincode.com/home/

地址：
1.python中,相同的值(数值?)共享同一地址,赋值会改变变量的地址
a = 5
b = a
c = 5
print(id(a),id(b),id(c))
>>2007549744 2007549744 2007549744
a = 6
print(id(a),id(b))
>>2007549776 2007549744

2.list的地址为总地址，总地址再指向元素地址？
a = [1,2,3]
b = a
print(id(a),id(b))
1406329761096 1406329761096

a.append(4)
print(a,b)
[1, 2, 3, 4] [1, 2, 3, 4]
print(id(a),id(b))
1406329761096 1406329761096

3.各自创建list,tuple时会赋予不同的地址
list1 = [1, 2, 3, 4, 5 ]
list2 = [1, 2, 3, 4, 5 ]
print(list1,id(list1),list2,id(list2))
>>[1, 2, 3, 4, 5] 1722411040392 [1, 2, 3, 4, 5] 1722411056200


更具体的列表地址有关请翻看note1.2_列表.py文件

在 python 中，类型(string)属于对象("Runoob")，变量(a)是没有类型的：
a=[1,2,3]
a="Runoob"
以上代码中，[1,2,3] 是 List 类型，"Runoob" 是 String 类型，
而变量 a 是没有类型，她仅仅是一个对象的引用（一个指针(指向某个地址的值)）,
可以是 List 类型对象，也可以指向 String 类型对象。

更具体的变量、对象与类型请看note4_函数.py

#small values cashing
>>> a = 1000000
>>> b = 1000000
>>> id(a) == id(b)
False
>>> a = 5
>>> b = 5
>>> id(a) == id(b)
True
Oh oh! Is Python broken? Why are the two objects the same now? We didn't do a =
b = 5, we set them up separately. Well, the answer is performances. Python caches
short strings and small numbers, to avoid having many copies of them clogging up
the system memory. Everything is handled properly under the hood so you don't
need to worry a bit, but make sure that you remember this behavior should your
code ever need to fiddle with IDs.


运算
(一)比较运算符
> : 大于
< : 小于
>= : 大于等于
<= : 小于等于
== : 等于(区分开赋值=)
!= : 不等于
not() :否
and :并
or :或
不能用三个或以上的and、or运算
——————————————————————————
(二)算术运算符
+ : 加
- : 减
* : 乘
** : 求n次方
/ : 除
% : 求余数
// : 除法取整 (-7//4 = -2哦~, 不过可以用int(-7/4) = -1)
divmod() :  返回一个(取整,余数)的tuple  
——————————————————————————
(三)赋值运算符
3.1 简单赋值 : =

3.2 多变量赋值 
a = b = c = 1
a, b, c = 1, 2, "runoob"
注：多变量赋值遵循从右到左的顺序

3.3特殊赋值 : += -= *= **= /= %= //=
int0 = int0 + n 可以写成
int0 += n

——————————————————————————
(四)布尔运算符
4.1 三个布尔运算符
and 
or
not
注：
0和1在逻辑值判断时，0会被视同于False，1会被视同于True

4.2 特殊技巧：(bool and [a] or [b])[0]

在一个bool and a or b语句中，当bool条件为真时，结果是a；当bool条件为假时，结果是b
a = "a"
b = "b"
print(True and a or b)
>>a
print(False and a or b)
>>b

可以用来替代代码块:
if a > 0:
    print "big"
else:
    print "small"
print((a > 0) and "big" or "small")

但a不能为假值，如："", 0 
可改写为list确保a不为假值
(bool and [a] or [b])[0]
a = 0
b = "b"
print(True and a or b)
>>b
print(False and a or b)
>>b
print((True and [a] or [b])[0])
>0
print((False and [a] or [b])[0])
>>b

——————————————————————————
(五)成员运算符
in
not in

eg.
a = 1
list = [1, 2, 3, 4, 5 ];
print(a in list)            
>>True
——————————————————————————
(六)身份运算符
is - 判断两个标识符是不是引用自一个对象 类似id(x) == id(y)
not is

a = 1
b = 1
print(a is b)
>>True
print(id(a)," ",id(b))
>>2002568880 2002568880

a = [1,2,3]
b = a[:]

print(b is a)
>>False
print(id(a),id(b)) 
>>1927764978952 1927765802632

print(b == a)
>>True
print(a,b)
>>[1, 2, 3] [1, 2, 3]
——————————————————————————



"""