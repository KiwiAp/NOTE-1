from multiprocessing import Process, Pool, Queue
import threading 
import os, time, random

'''
os.getpid() - 返回自身ID
os.getppid() - 返回父进程ID

multiprocessing:
Process(target,args) - 类,创建子进程,target是子进程地址空间,args是传入参数
Pool() - 类,创建进程池
Pool.apply_async(target,args) - 实例方法,创建子进程,target是子进程地址空间,args是传入参数
start() - 实例方法,启动子进程
end() - 实例方法,终止子进程
join() - 实例方法,等待进程终止
terminate() - 实例方法,终止进程


Queue() - 类,进程通信队列
Queue.put() - 实例方法,往队列里放入数据
Queue.get() - 实例方法,从队列里取出数据

threading:
Thread(target,args) - 类,创建线程,target是子进程地址空间,args是传入参数
start() - 实例方法,启动子线程
end() - 实例方法,终止子线程
join() - 实例方法,等待线程终止
terminate() - 实例方法,终止进程
getname() - 获得当前线程名字
threading.current_thread().name - 当前线程名字
setDaemon(bool)
'''
