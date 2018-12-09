"""

(一)命令行的类型
1.cmd
2.power shell

(二)启动方式
win+R , 输入cmd/powershell

(三)powershell有关python的教学
1.打开python
>python
2.退出python
>quit()
3.打开某个.py文件
>python C:\Pyhon36\文件名.py  (python 文件地址 文件名)
4.打开python说明书
>python –m pydoc -b
>python –m pydoc print (函数名)

(四)powershell的目录教学
0.powershell不区分大小写
1.查看当前目录(print working directory)
>pwd 
2.移动到某目录(change directory)
>cd 目录名
>cd desktop(目标目录必须在当前目录下)
>cd desktop\others things
>d: (移动到其他盘)
3.目录快捷键： 
~ 用户主目录
\  根目录
.\  当前目录
..\ 上级目录
4.创建目录(make directory)
>mkdir 目录名
>mkdir text
>mkdir text\apple\banae\car\dogs
5.列出当前目录下的内容(list)
>ls
6.清除powershell的界面(cleans)
>cls
7.移动目录(move)
>mv 源 目标
>mv text TTT
如果目标目录存在，则会放入目标目录下
若果目标目录不存在，则会重命名为目标目录
8.复制目录(copy)
>cp 源 目标
9.删除目录(remove)
>rm 目录名
10.退出命令行
>exit
11.查询所有分支
>tree

"""