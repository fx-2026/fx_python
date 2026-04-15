import os
from multiprocessing import Process
import time
#参数Process(group=None,target=None,name=None,args=(),kwargs={})
#group :分组，实际上很少使用
#target:表示调用对象，你可以传入方法名字
#name:给进程取个别名
#args:表示被调用对象的位置参数元组
#kwargs:表示调用对象的字典

# def child_task():
#     print(f"子进程执行中，PID: {os.getpid()}")
#
#
# if __name__ == '__main__':
#     print(f"父进程PID: {os.getpid()}")
#
#     # 创建子进程
#     p = Process(target=child_task)
#     p.start()
#
#     print(f"父进程等待子进程 {p.pid} 结束")
#     p.join()  # 等待子进程结束
#
#     print("子进程已结束")

def f(name):
    print(f'hello {name}')
    print('子进程开始')
    time.sleep(5)
    print('子进程结束')

if __name__ == '__main__':
    print('父进程开始')
    p = Process(target=f,args=('join',))#必须元组格式，要加个逗号
    p.start()#启动进程
    p.join()#等子进程结束后父进程再结束
    print('父进程结束')
