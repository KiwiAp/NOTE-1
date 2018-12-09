"""
数据结构：

堆栈： [……]← →
列表方法使得列表可以很方便的作为一个堆栈来使用，堆栈作为特定的数据结构，最先进入的元素最后一个被释放（后进先出）。
用 append() 方法可以把一个元素添加到堆栈顶。用不指定索引的 pop() 方法可以把一个元素从堆栈顶释放出来。

队列： ←[……]←
也可以把列表当做队列用，只是在队列里第一加入的元素，第一个取出来；但是拿列表用作这样的目的效率不高。
在列表的最后添加或者弹出元素速度快，然而在列表里插入或者从头部弹出速度却不快（因为所有其他的元素都得一个一个地移动）。


列表推导式：
list = list(range(5))
list = [i for i in range(0,15)]
list2 = [i*2 for i in list1]
list2 = [[i,i*2] for i in list1]
list2 = [i*2 for i in list1 if i > 3]
# 集合,字典也兼容推导式
list_L = [0 for i in range(5)]
list_L = [0]*5

列表推导式的执行顺序：各语句之间是嵌套关系，左二是最外层，依次往右深一层，左一是最内层。
[x*y for x in range[1,5] if x > 2 for y in range[1,4] if x < 3]
它的执行顺序是
for x in range[1,5]
    if x > 2
        for y in range[1,4]
            if x < 3
                x*y

但中括号可以提高优先级
list = [[1, 2, 3, 4],[5, 6, 7, 8],[9, 10, 11, 12]]
[[print(row[i]) for row in list] for i in range(4)]
推导语句，应该先执行最右侧的 for，但是左侧的for用[]括起来，所以它的优先级提高了，会被先执行
它的执行顺序是
for i in range(4):
    for row in list:
        print(row[i])
相等于[print(row[i]) for i in range(4) for row in list]
注意是括号是中括号[],如果用了小括号()程序会误以为这是生成器generater


矩阵列表(嵌套列表)：
list = [
    [1,2,3,4]
    [5,6,7,8]
    [9,10,11,12]
]           #3×4矩阵表
[[row[i] for row in list] for i in range(4)]        #列表的倒置：转化成4×3矩阵表


历遍技巧:
在字典中遍历时，关键字和对应的值可以使用 items() 方法同时解读出来
for key, value in dict.items():

在序列中遍历时，索引位置和对应值可以使用 enumerate() 函数同时得到
for x, y in enumerate(list):

【enumerate()是python的内置函数
enumerate在字典上是枚举、列举的意思
对于一个可迭代的（iterable）/可遍历的对象（如列表、字符串），enumerate将其组成一个索引序列，利用它可以同时获得索引和值
enumerate多用于在for循环中得到计数
例如对于一个seq，得到：
(0, seq[0]), (1, seq[1]), (2, seq[2])
enumerate()返回的是一个enumerate对象】

同时遍历两个或更多的序列，可以使用 zip() 组合
list1 = [a,b,c,d,e]
list2 = [1,2,3,4,5]
for x,y in zip(list1,list2):

要反向遍历一个序列，首先指定这个序列，然后调用 reversed() 函数
list = reversed(list)

要按顺序遍历一个序列，使用 sorted() 函数返回一个已排序的序列，并不修改原值
list = [1,5,3,2,4]
for i in sorted(list):
    print(i,end = " ")
>>1 2 3 4 5



列表List:

(一) [] - 方括号 - Python 访问列表内元素，可以使用方括号来截取列表，具体如同字符串

(二) 列表操作符
3.1 + 组合
print([1, 2, 3] + [4, 5, 6])
>>[1, 2, 3, 4, 5, 6]

3.2 * 重复
print(['Hi!'] * 4)
>>['Hi!', 'Hi!', 'Hi!', 'Hi!']

*3.3 range 技巧 - 创建1到i的列表
list_0 = list(range(1,i+1))

3.4 del - 删除列表
del list

3.5 len() - 查询列表长度
value = len(list)

3.6 in - 查询元素是否存在
x = value in list

3.7 for i in list: - 迭代、历遍list中所有元素


(三) 嵌套列表
a = [1,2,3]
b = [4,5,6]
c = [a,b]
print(c)
>>[[1,2,3],[4,5,6]]
print(c[1][2])
>>2

(四) 列表的函数和方法：

查询类：
len() - 列表元素个数
max() - 返回列表元素最大值
min() - 返回列表元素最小值
list.count() - 统计某个元素在列表中出现的次数
list.index() - 从列表中找出某个值第一个匹配项的索引位置

计算list中最多的一项
count_list = {}
for term in kNN_list: 
    count_list[term] = count_list.get(term, 0) + 1
sorted([ (freq,digit) for digit, freq in count_list.items()], reverse=True)


处理类：
list.append() - 在列表末尾添加新的对象
list.extend() - 用新列表加到原来的列表后(比+的效率更高，但不能返回值)
list.extend(range(1,num+1)) - 也可以加iter的对象！
list.insert() - 将对象插入列表
#！
list.pop() - 移除列表中的一个元素，并且返回该元素的值
list.remove() - 移除列表中某个值的第一个匹配项
#永远，永远。永远！不要在一个循环里面删除list的元素！！！！！
#不要在for i in list:中用list.remove!因为remove后所有项的序号会往前移导致remove后面那个项没有被历遍到
list.reverse() - 反向列表中元素
list.sort() - 对原列表进行排序
list.clear() - 清空列表

list.copy() - 用于复制列表()

注：copy方法(浅复制)与赋值的不同(python中对地址的概念):

1.赋值共享总列表地址,copy不共享总列表地址
a = [1,2,3]
b = a
c = a.copy()

a.append(4)
b.append(5)
c.append(6)
print(a,b,c)
>>[1,2,3,4,5],[1,2,3,4,5],[1,2,3,6]
print(id(a),id(b),id(c))
2424202669384 2424202669384 2424203493000
赋值的话,a,b共用地址,任意一个改变就会改变另一个的值
copy的话,创建了新地址，改变互不影响

2.赋值共享总列表地址,copy共享列表第一层元素地址
a = [1,[2,3],4]
c = a.copy()        # c = a[:]也是一样的浅copy
a[1].append(5)
print(c)
>>[1, [2, 3, 5], 4]

因为copy共享了第一层元素的地址，如果第一层某元素是个嵌套列表，那么它的改变就会影响接受copy的元素

3.如果想copy深层列表的全部地址的话,用deepcopy(深复制)
import copy
a = [1,[2,3],4]
c = copy.deepcopy(a)
a[1].append(5)
print(c)
>>[1, [2, 3], 4]
这样我们就可以获得一个完全不发生改变的list
'''