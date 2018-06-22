"""
OS文件/目录方法

内核（kernel）利用文件描述符（file descriptor）来访问文件。文件描述符是非负整数。
打开现存文件或新建文件时，内核会返回一个文件描述符。读写文件也需要使用文件描述符来指定待读写的文件。

open（），它返回的是文件对象。
os.open() ,它返回的是一个文件描述符

文件描述符：
(进程表)文件描述符表 --> 打开文件表 --> i-node表
http://www.ruanyifeng.com/blog/2011/12/inode.html
http://blog.csdn.net/u013078669/article/details/51172429
http://blog.csdn.net/cywosp/article/details/38965239
https://www.jianshu.com/p/dde6a01c4094
https://www.cnblogs.com/how-are-you/p/5699257.html


所有方法：http://www.runoob.com/python3/python3-os-file-methods.html

权限：
os.access - 检验权限模式
os.chmod - 更改权限
os.chown - 更改文件所有者

路径信息查询：
os.stat(path) - 获取path指定的路径的信息，功能等同于C API中的stat()系统调用。
os.stat_float_times([newvalue]) - 决定stat_result是否以float对象显示时间戳
os.statvfs(path) - 获取指定路径的文件系统统计信息
os.fstat - 返回文件描述符fd的状态，像stat()
os.lstat(path) - 像stat(),但是没有软链接
os.fstatvfs - 返回包含文件描述符fd的文件的文件系统的信息，像 statvfs()
os.utime(path, times) - 返回指定的path文件的访问和修改的时间。

工作目录处理：
os.getcwd() - 返回当前工作目录
os.getcwdu() - 返回一个当前工作目录的Unicode对象
os.chdir - 改变当前工作目录
os.chroot - 改变当前进程的根目录
os.fchdir - 通过文件描述符改变当前工作目录

file处理：
os.open(file, flags[, mode]) - 打开一个文件，并且设置需要的打开选项，mode参数是可选的
os.read(fd, n) - 从文件描述符 fd 中读取最多 n 个字节，返回包含读取字节的字符串，文件描述符 fd对应文件已达到结尾, 返回一个空字符串。
os.write(fd, str) - 写入字符串到文件描述符 fd中. 返回实际写入的字符串长度
os.lseek(fd, pos, how) - 设置文件描述符 fd当前位置为pos, how方式修改: SEEK_SET 或者 0 设置从文件开始的计算的pos; SEEK_CUR或者 1 则从当前位置计算; os.SEEK_END或者2则从文件尾部开始. 在unix，Windows中有效
os.close - 关闭文件描述符 fd
os.closerange - 关闭所有文件描述符，从 fd_low (包含) 到 fd_high (不包含), 错误会忽略
os.ftruncate(fd, length) - 裁剪文件描述符fd对应的文件, 所以它最大不能超过文件大小。

os.dup - 复制文件描述符 fd         #但好像直接赋值也可以？
os.dup2 - 将一个文件描述符 fd 复制到另一个 fd2

文件/目录处理：
os.listdir(path) - 返回path指定的文件夹包含的文件或文件夹的名字的列表。
os.walk(top[, topdown=True[, onerror=None[, followlinks=False]]]) - 输出在文件夹中的文件名通过在树中游走，向上或者向下。
os.mkdir(path[, mode]) - 以数字mode的mode创建一个名为path的文件夹.默认的 mode 是 0777 (八进制)。(mode指示权限)
os.makedirs(path[, mode]) - 递归文件夹创建函数。像mkdir(), 但创建的所有intermediate-level文件夹需要包含子文件夹。
os.rmdir(path) - 删除path指定的空目录，如果目录非空，则抛出一个OSError异常。
os.remove(path) - 删除路径为path的文件。如果path 是一个文件夹，将抛出OSError; 查看下面的rmdir()删除一个 directory。
os.removedirs(path) - 递归删除目录。
os.unlink(path) - 删除文件路径
os.rename(src, dst) - 重命名文件或目录，从 src 到 dst
os.renames(old, new) - 递归地对目录进行更名，也可以对文件进行更名。


管道：https://baike.baidu.com/item/FIFO%E7%AE%A1%E9%81%93/8466221?fr=aladdin
http://blog.csdn.net/firefoxbug/article/details/8137762
os.mkfifo(path[, mode]) - 创建命名管道，mode 为数字，默认为 0666 (八进制)
os.pipe() - 创建一个管道. 返回一对文件描述符(r, w) 分别为读和写
os.popen(command[, mode[, bufsize]]) - 从一个 command 打开一个管道

节点：
os.mknod(filename[, mode=0600, device]) - 创建一个名为filename文件系统节点（文件，设备特别文件或者命名pipe）。

链接：https://www.jianshu.com/p/dde6a01c4094   
https://zhidao.baidu.com/question/940879051762143092.html
http://m.elecfans.com/article/600527.html
http://blog.sina.com.cn/s/blog_6b5a07450102vljd.html
硬连接指向的是节点(inode)(硬盘的实际位置,经纬度)，而软连接指向的是路径(path)(硬盘的名义位置,门牌号) 。
指向同一个节点的多个文件相当于同一个文件,不分高下。
指向同一个路径的文件,如果主文件(路径文件)删除,则其它指向该路径的文件全部失效
软链接!=快捷方式(一种名为.lnk的文件类型,可是为一种软件,会占一定的空间,较低权限就可获得,有着跟软链接差不多的功能,但实现机制大相径庭)
os.link(src, dst) - 创建硬链接，名为参数 dst，指向参数 src
os.symlink(src, dst) - 创建一个软链接          
#要用"以管理员身份运行"VScode,否则会权限不够.也可以用命令提示符(管理员权限)输入mklink创建
os.readlink(path) - 返回软链接所指向的文件



windows用不了：
os.chflags - 设置路径的标记为数字标记(更改权限)(unix可用)
os.lchflags(path, flags) - 设置路径的标记为数字标记，类似 chflags()，但是没有软链接(unix可用)
os.fdatasync - 强制将文件写入磁盘，该文件由文件描述符fd指定，但是不强制更新文件的状态信息 (unix可用)
os.fpathconf - 返回一个打开的文件的系统配置信息。name为检索的系统配置的值，它也许是一个定义系统值的字符串，这些名字在很多标准中指定（POSIX.1, Unix 95, Unix 98, 和其它）(unix可用)
os.lchmod(path, mode) - 修改连接文件权限(unix可用)
os.lchown(path, uid, gid) - 更改文件所有者，类似 chown，但是不追踪链接。(unix可用)
os.fchmod - 改变一个文件的访问权限，该文件由参数fd指定，参数mode是Unix下的文件访问权限。(unix可用)
os.fchown - 修改一个文件的所有权，这个函数修改一个文件的用户ID和用户组ID，该文件由文件描述符fd指定(unix可用)
os.fsync - 强制将文件描述符为fd的文件写入硬盘(unix可用)
os.pathconf(path, name) - 返回相关文件的系统配置信息。(unix可用)

os.major(device) - 从原始的设备号中提取设备major号码 (使用stat中的st_dev或者st_rdev field)。
os.minor(device) - 从原始的设备号中提取设备minor号码 (使用stat中的st_dev或者st_rdev field )。
os.makedev(major, minor) - 以major和minor设备号组成一个原始设备号

os.isatty(fd) - 如果文件描述符fd是打开的，同时与tty(-like)设备相连，则返回true, 否则False。
tty是什么:http://blog.csdn.net/bdss58/article/details/77779672
os.openpty() - 打开一个新的伪终端对。返回 pty 和 tty的文件描述符。
os.tcgetpgrp(fd) - 返回与终端fd（一个由os.open()返回的打开的文件描述符）关联的进程组
os.ttyname(fd) - 返回一个字符串，它表示与文件描述符fd 关联的终端设备。如果fd 没有与终端设备关联，则引发一个异常。

