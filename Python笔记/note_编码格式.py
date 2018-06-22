'''
1 byte = 8 bits
1位 十六进制 = 4位 二进制
1 byte = 2位 十六进制 = 8位 二进制 
1 字符 = "a","我","?" ……

1)ASCII : 
时间 : 1967
内容 : 控制字符、数字、英文字符
格式 : 1 byte
(0口口口 口口口口) 
容量 : 2**7=128
详情 : 
0~31+127 控制字符(换行、回车),不可打印
48~57 数字
65~90 大写字母
97~122 小写字母
其它 其它符号


2)扩展ASCII : 
时间 : 1981
内容 : ASCII + 欧洲其它语言字符
格式 : 1 byte
(口口口口 口口口口)
容量 : 2**8=256
详情 : 
(0口口口 口口口口) ASCII编码
(1口口口 口口口口) 欧洲其它语言字符


3)unicode : 
时间 : 1994
内容 : ASCII + 世界所有语言字符(编码方式 : 规定代码)
格式 : 2 byte(USC-2,零号平面)(U+表示) , 4 byte(USC-4)(U-表示)
()() , ()()()()
容量 : 
1平面 - 后 2 byte(容量2**16=65536)
17平面 65536*17=1114112
详情 : 
Big endian - 文件开头FE FF(BOM:Byte Order Mark) , 组成1个字符的2个byte顺序排列
little endian - 文件开头FF FE , 组成1个字符的2个byte逆序排列

unicode的转换格式 : (转换格式 : 规定储存)
1.UTF-8 (1~4 byte) (文件开头EF BB BF)(从unicode里二进制逐位填充)
(0口口口 口口口口) ASCII编码 - U+0000~U+007F
(110口 口口口口)(10口口 口口口口) - U+0080~U+07FF
(1110 口口口口)(10口口 口口口口)(10口口 口口口口) - U+0800~U+FFFF
(1111 0口口口)(10口口 口口口口)(10口口 口口口口)(10口口 口口口口) - U-0001 0000~U-0010 FFFF
2.UTF-16 (2,4 byte) (实际上这就是unicode)
3.UTF-32 (4 byte)
#为什么unicode编码还要专门配转换格式呢?
1.节省空间 : 世界上大部分字符都是英文字符,只要用1 byte就可以表达,大部分情况下用2 byte甚至是4 byte就是一种浪费

举例 : "严"字从unicode转到UTF-8
unicode : U+4E25 - (0100 1110)(0010 0101)
UTF-8 : ∵U+4E25∈(U+0800~U+FFFF) ∴(1110 口口口口)(10口口 口口口口)(10口口 口口口口)
(1110 0100)(1011 1000)(1010 0101) - E4 B8 A5
即从 U+4E2F 转到 E4B8A5
#汉字在unicode里面属于U+4E00~U+9FA5区间，所以UTF-8码都是3 byte

4)DBCS系列 : 
#DBCS系列与扩展ASCII和unicode是不兼容的
GB2312 : 
时间 : 1981
内容 : ASCII + 汉字6763个
格式 : 
(0口口口 口口口口) ASCII编码
(1口口口 口口口口)(1口口口 口口口口) 汉字

GBK : 
时间 : 1995
内容 : GB2312 + 更多汉字 (共21003个)
格式 : 
(0口口口 口口口口) ASCII编码
(1口口口 口口口口)(口口口口 口口口口) 汉字

GB18030
时间 : 2000,2005
内容 : GBK + 更多汉字

5)Big5 : 
时间 : 1984
内容 : 繁体汉字

6)CJK:
内容 : 中国文字 + 日本文字 + 韩国文字
格式 : 属于unicode
详情 : 在unicode的U+4E00~U+9FBF区间

7)ANSI:
内容 : ASCII + 国家自定义 (ANSI没有BOM)
格式 : 1 byte , 2 byte
详情 : (windows系统下)
简体中文 - GBK
繁体中文 - Big5
日文 - Shift_JIS
……
不同的ANSI编码之间不兼容



(8)python的编码详解:
python的默认编码方式是utf-8, sys.getdefaultencoding()='utf-8'
字符要被写进文件、存进硬盘或者从服务器发送至客户端（例如网页前端的代码）时会变成utf-8

但python的string object用的是unicode编码,以二进制的形式储存在内存中
python终端上会把二进制按unicode编码转换成字符显示出来

>>> a = 'abcd吴'
>>> tpye(a)
<class 'str'>
>>> a
'abcd吴'

如果用string的encode方法(编码)可以将对象转为bytes类,以指定的编码方式
>>> b = a.encode('utf-8')
>>> type(b)
<class 'bytes'>
>>> b
b'abcd\xe5\x90\xb4'

注:实际上我们知道，正确结果应该为b'\x61\x62\x63\x64\xe5\x90\xb4'
在python中\的转译对终端显示的影响:
\x**表示用2个十六进制来表示一个字符,
\o**表示用2个8进制来表示一个字符,
\***表示用3个8进制来表示一个字符 
\u****表示以unicode编码用4个16进制来表示一个字符(等价于string)

b' '表示这是bytes类型,print的时候会把能用ASCII表达的字符(\x61)显示出来
' '表示这是string类型,print的时候会把能用扩展ASCII表达的字符(\xe5)显示出来
r' '表示这是没有转译的string类型,print的时候会老老实实地print

>>> '严'.encode()
b'\xe4\xb8\xa5'
>>> '严'.encode('utf-8')
b'\xe4\xb8\xa5'
>>> '严'.encode('unicode-escape')
b'\\u4e25'
>>> '严'.encode('gbk')
b'\xd1\xcf'

>>> b'\xe4\xb8\xa5'.decode()
'严'

>>>b'\\u4e25'.decode('unicode-escape').encode()    #将unicode码转换到utf-8码
b'\xe4\xb8\xa5'


(9)笔记本的趣事:
在笔记本中输入"姹塧"并保存,下次打开的时候就会变成"汉a"
因为windows的笔记本的默认保存方式是ANSI(gbk),而"姹塧"的gbk编码是"\xe6\xb1\x98\x61"
而windows的笔记本在打开的时候,如果开头有BOM,那就按BOM的指示去解码
如果开头没有BOM,首先会优先尝试用uft-8来解码,如果不行就再用会ANSI(gbk)
而"汉a"的uft-8编码恰好也是"\xe6\xb1\x98\x61"……

输入"联通"下次打开时会变成"��ͨ"乱码
因为"联"的gbk码刚好可以开启utf-8,而"通"的gbk码被utf-8解析出错，导致全部变成乱码
但如果后面多输几个字,笔记本就能意识到,哦,这不是utf-8而是ANSI
'''

