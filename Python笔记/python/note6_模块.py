
模块：

资源：http://wecatch.me/blog/2016/05/28/python-module-path-find/
http://kuanghy.github.io/2016/07/21/python-import-relative-and-absolute
http://www.runoob.com/python3/python3-module.html
https://www.cnblogs.com/ArsenalfanInECNU/p/5346751.html
https://segmentfault.com/a/1190000010731855


1.模块注释

标准注释:
#!/usr/bin/env python3
# -*- coding: utf-8 -*-

文档注释:
'……'

作者:
__author__ = '……'

第1行注释可以让这个文件直接在Unix/Linux/Mac上运行
第2行注释表示.py文件本身使用标准UTF-8编码
第3行是一个字符串，表示模块的文档注释，任何模块代码的第一个字符串都被视为模块的文档注释
第4行使用__author__变量把作者写进去，这样当你公开源代码后别人就可以瞻仰你的大名


问：为什么我没建__init__.py都可以自由引用？
这一课包那里非常懵逼

python 解释器执行的时候,搜索已导入模块的顺序：
built-in module --> sys.path(执行文件所在目录 --> 其他path上的文件)
注：文件所在的文件夹会被加入 sys.path 的首位,可用sys.path查看,
注：但！用A文件引用B文件,B文件引用C文件时,添加入path的仅是A文件的父目录,B文件的父目录是没有加入path的

所以python包的导入顺序：
系统包 --> 同目录 --> sys.path

几个函数：
print(__file__)             #模块文件的路径名
print(sys.argv[0])          #用来获取主入口执行文件的变量
print(sys.modules["laugh"])         #查询modules中已载入的模块
注：python 所有加载的模块信息都存放在 sys.modules 结构中

print(os.path.realpath(sys.modules['laugh'].__file__))        #查询modules中已载入的模块的绝对地址



module：模块， 一个 py文件或以其他文件形式存在的可被导入的就是一个模块

package：包，包含有 __init__ 文件的文件夹

relative path：相对路径，相对于某个目录的路径

absolute path：绝对路径，全路径

路径查找：python 解释器查找被引入的包或模块

(一)查询python模块的搜索路径:
import sys
print(sys.path)
#第一个空字符串是当前目录


(二)引入模块：
import ……       - 引入……模块
引用函数的时候要写成sys.path
/
from …… import ……  - 从……模块引入……项目
引用函数的时候要写成path
/
from …… import *   - 从……模块引入所有项目
引用函数的时候要写成path
这将把所有的名字都导入进来，但是那些由单一下划线（_）开头的名字不在此例。
大多数情况， Python程序员不使用这种方法，因为引入的其它来源的命名，很可能覆盖了已有的定义。

(三)给引入的模块的函数赋给一个本地的名称：
import sys
path = sys.path
print(path)


关于地址的问题……
要注意的是,比如说python的搜索地址到C:\\Python36 , 而你想引用的模块在C:\\Python36\\file\\bao .
from的时候一定要写from file.bao import xxx啊！一定要写搜索地址的下属模块啊！哭啊！

或者添加搜索路径：
import sys
sys.path.append("c:\\Python36\\file")

执行py时会自动把当前文件的父目录加入path


(四)__name__属性
一个模块被另一个程序第一次引入时，其主程序将运行。
如果我们想在模块被引入时，模块中的某一程序块不执行，我们可以用__name__属性来使该程序块仅在该模块自身运行时执行。
if __name__ == '__main__':
   print('程序自身在运行')
else:
   print('我来自另一模块')
运行输出如下：
$ python using_name.py
程序自身在运行
$ python
>>> import using_name
我来自另一模块
>>>
说明： 每个模块都有一个__name__属性，当其值是'__main__'时，表明该模块自身在运行，否则(值为模块的名字)是被引入。

(五)dir()函数
内置的函数 dir() 可以找到模块内定义的所有名称,并以一个字符串列表的形式返回
dir(sys)
如果没有参数,那么 dir() 函数会罗列出当前定义的所有名称
dir()




(六)包
不妨假设你想设计一套统一处理声音文件和数据的模块（或者称之为一个"包"）。
现存很多种不同的音频文件格式（基本上都是通过后缀名区分的，例如： .wav，:file:.aiff，:file:.au，），
所以你需要有一组不断增加的模块，用来在不同的格式之间转换。
并且针对这些音频数据，还有很多不同的操作（比如混音，添加回声，增加均衡器功能，创建人造立体声效果），所
以你还需要一组怎么也写不完的模块来处理这些操作。

注：而且也是为了避免不同人写的模块名冲突,因为有了包之后,模块名前面都加上了包前缀

这里给出了一种可能的包结构（在分层的文件系统中）:
sound/                          顶层包
      __init__.py               初始化 sound 包
      formats/                  文件格式转换子包
              __init__.py
              wavread.py
              wavwrite.py
              aiffread.py
              aiffwrite.py
              auread.py
              auwrite.py
              ...
      effects/                  声音效果子包
              __init__.py
              echo.py
              surround.py
              reverse.py
              ...
      filters/                  filters 子包
              __init__.py
              equalizer.py
              vocoder.py
              karaoke.py
              ...

在导入一个包的时候，Python 会根据 sys.path 中的目录来寻找这个包中包含的子目录。
目录只有包含一个叫做 __init__.py 的文件才会被认作是一个包，(__init__.py可以空,也可以写程序,相对引用到包时会先调用包上的__init__.py)
主要是为了避免一些滥俗的名字（比如叫做 string）不小心的影响搜索路径中的有效模块。

注意当使用from package import item这种形式的时候，
对应的item既可以是包里面的子模块（子包），或者包里面定义的其他名称，比如函数，类或者变量。
import语法会首先把item当作一个包定义的名称，如果没找到，再试图按照一个模块去导入。
如果还没找到，恭喜，一个:exc:ImportError 异常被抛出了。

反之，如果使用形如import item.subitem.subsubitem这种导入形式，
除了最后一项，都必须是包，而最后一项则可以是模块或者是包，但是不可以是类，函数或者变量的名字。

在windos下面,尽量不要试图用from package import *来导入包
如果实在要用,详情请看:http://www.runoob.com/python3/python3-module.html

(七)相对导入！：
7.1 相对引用只能用在包结构上
7.2 文件夹被python解释器视作package(包)需要满足两个条件：

　　1、文件夹中必须有__init__.py文件，该文件可以为空，但必须存在该文件。

　　2、不能作为顶层模块来执行该文件夹中的py文件（即不能作为主函数的入口）。
注：即你想在karaoke.py中from . import vocoder 是非法的,
因为运行karaoke.py时,karaoke是主函数的入口,python不把filters视为包

而如果是在与filters同级的main.py文件(假设有)上引用到karaoke.py时,这时karaoke.py中from . import vocoder 是合法的,
因为这时python把sound不视为包,而把sound下属的filter视为包,有包的话,相对引用就可以使用了
https://www.cnblogs.com/ArsenalfanInECNU/p/5346751.html

注：如果一个模块被直接运行，则它自己为顶层模块，不存在层次结构，所以找不到其他的相对路径。
即：哪个模块被运行，就由哪个模块为基准来确定层次结构

7.3 一般推荐相对引用,利于版本维护

7.4
•如果是绝对导入，一个模块只能导入自身的子模块或和它的顶层模块同级别的模块及其子模块
•如果是相对导入，一个模块必须有包结构且只能导入它的顶层模块内部的模块
