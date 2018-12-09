"""
基本函数:


(一)print函数
1.print(value),value可为数值、字符串、变量、算式
2.print(value1,value2),可连接两个量
3.默认下，print后会自动换行；print(value,end = "")可不换行
4.print()可换行；print("\n或\t")可换行/缩进
5.可换行续写print,这里以-标记换行点
print(-value1-,-value2-)
或者
print("……\
……")
或者
print("""……(\)
……""")
6.有点需要注意的是,如果不换行的话(end = ""),python会把该行需要输出的东西储存起来,等这行输出结束以后
在把所有东西一次性print上去,而不是一个一个print上去,这在迭代器的使用时会经常发生\
7.repr()函数相当于直接在终端中输入变量
——————————————————————————
(二)input函数
1.A = input(),输出的A为字符串
2.A = eval / int(input()),将输出的A转化为可用格式
3.A = input("……"),可打出……并使输入在……右侧而不换行
——————————————————————————
(三)if函数
1.
if A > B:
    ……
elif A < B:
    ……
else:
    ……
……
2.缩写
var = 1 if A > B else 2
——————————————————————————
(四)while函数
1.
while A<B :
    ……
    A=A+1
……
——————————————————————————
(五)for函数
1.
for i in range(a,b)/range(1,5,6,23)/string/list/tuple/dictionary :
    ……
……
2.i将历遍[a,b)或者说[a,b-1],所以一般推荐写成 for i in range(a,b+1):方便阅读
3.可以与list复合使用：list(range(5))
或者l = [i for i in range(0,15)]

4.enumerate配合迭代,返回下标(重要！)
>>> for i, value in enumerate(['A', 'B', 'C']):
...     print(i, value)
...
0 A
1 B
2 C

5.同时获取多个数据
>>> for x, y in [(1, 1), (2, 4), (3, 9)]:
...     print(x, y)
...
1 1
2 4
3 9

6.for循环的迭代本质
Python的for循环本质上就是通过不断调用next()函数实现的，例如：

for x in [1, 2, 3, 4, 5]:
    pass
实际上完全等价于：

# 首先获得Iterator对象:
it = iter([1, 2, 3, 4, 5])
# 循环:
while True:
    try:
        # 获得下一个值:
        x = next(it)
    except StopIteration:
        # 遇到StopIteration就退出循环
        break

7.实用的骚用法！
for _ in range(n): - 在一个循环中不关系具体的值的时候的用法
如果想说明_的意义也可以
for _picture in range(n):
——————————————————————————
(六)try函数
try:
    ……
except:
    ……
——————————————————————————
(七)continue语句
用于跳过本层的本次循环
——————————————————————————
(八)break语句
用于跳过本层的所有循环
——————————————————————————
(九)pass语句
空语句

(十)zip函数 - 胶水函数 - 返回一个iterator
>>> list(zip(['h', 'e', 'l', 'l', 'o'], [1, 2, 3, 4, 5]))
[('h', 1), ('e', 2), ('l', 3), ('l', 4), ('o', 5)]
>>> list(zip('hello', range(1, 6))) # equivalent, more Pythonic
[('h', 1), ('e', 2), ('l', 3), ('l', 4), ('o', 5)]

(十一)for/while后面跟的else:
for ...:
    ...
else:
    ...

或者
while ...:
    ...
else:
    ...

的写法是没问题的，else语句会在for或while循环正常完成后触发,如果循环被中断(break)而停止则不会触发

例子：
primes = []
upto = 100
for n in range(2, upto + 1):
    for divisor in range(2, n):
        if n % divisor == 0:
            break
    else:
    primes.append(n)
print(primes)