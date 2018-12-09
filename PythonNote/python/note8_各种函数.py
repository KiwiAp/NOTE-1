"""
(一)math.ceil函数：向上取整
Import math
A = math.ceil(X),A为X的向上取整

(二)randint函数：生成随机数
from random import randint
A=randint(a,b),A为从[a,b]中随机抽取一个整数,a、b都需为整数

(三)str函数：转化成字符串
A=str(),用来转化其他格式成文本

(四)eval函数：自动转化成对应格式
A=eval(),使……有效化，用来转化文本成数字,运算或其他格式

(五)argv函数：提取命令行参数
from sys import argv
变量1, 变量2,…… = argv
用来提取在命令行输入的参数，argv是参数变量(变量集)，Line2用来解包argv(将变量集里的变量分配下去)

eg.
python:
from sys import argy
name,a,v,c = argv
a = int(a)
b = int(b)
c = int(c)
if (b**2-4*a*c) >= 0
    result1 = (-b+(b**2-4*a*c)**0.5)/(2*a)
    result2 = (-b-(b**2-4*a*c)**0.5)/(2*a)
    print("The result is ",result1," and ",result2)
else:
    print("Error! Your result is not a real number)

命令行:
PS C:\users\Ezreal> python c:\python36\pracise.py 2 5 2
The result is -0.5 and -2.0



"""
