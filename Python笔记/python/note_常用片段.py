"""
标尺：ctrl+shift+p → open users setting →ruler "editor.rulers": []

html tags

attribute

"""

"""

检查并创建文件
try:
    file = open("c:/users/ezreal/desktop/test.txt","x")
    file.close
except:
    pass

打开文件
file = open("c:/users/levi/desktop/test.txt","w+")
file.close


优化输出
print("\n","-"*15,"start","-"*15)
print("-"*15,"end","-"*15)


打印文件内容
def printcode() :
    print(" ")
    file0 = open("c:/users/ezreal/desktop/test.py")
    print("***The code of this .py is :")
    print("-"*70)   
    print(file0.read())
    print("-"*70)
    file0.close()

字符串转化为二进制
bytes("This is test", 'UTF-8')
"This is test".encode()

动态生成变量
createVar = locals()            #locals() 函数会以字典类型返回当前位置的全部局部变量
for i,j in enumerate(range(1,10)):          #对于一个可迭代的或可遍历的对象j，enumerate将其组成一个索引序列(i,j)，利用它可以同时获得索引i和值j
    createVar['a'+str(i+1)] = j 
#似乎变量对于python来说就是储存在一个特殊字典里面的字符串！而locals()负责把这个特殊字典引出来,然后用来创造新的key(变量)

或
for i in range(1,10):
    locals()["a"+str(i)] = 0    




"""