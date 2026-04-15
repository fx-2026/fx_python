from multiprocessing import Process
import os
import multiprocessing

def info(title):
    print(title)
    print('module name:',__name__)
    print('parent process:',os.getppid())#父进程
    print('process id:',os.getpid())#子进程

def f(name):
    info('function f')
    print('hello',name)

if __name__ == '__main__':
    info('main')
    p = Process(target=f,args=('bob',))
    p.start()
    for p in multiprocessing.active_children():
        print(f'子进程名称：{p.name} id:{str(p.pid)}')
        print('进程结束')
    print(f'CPU核心数：{str(multiprocessing.cpu_count())}')
    p.join()

