#multiprocessing 支持进程之间的两种语言通道
#队列
#来自官方稳定的一个简单demo
#queue类似一个近似 queue.queue的克隆
#现在有这样一个需求：我们有两个进程，一个进程负责写（write)一个进程负责读（read).
#当写的进程写完某部分以后要不数据交给读的进程进行使用
#write（）将写完的数据交给队列，再由队列交给read()

# from multiprocessing import Process,Queue
# def f(q):
#     q.put([42,None,'hello'])#put是放入队列数据
#
# if __name__ == '__main__':
#     q = Queue()
#     p = Process(target=f,args=(q,))#p
#     p.start()
#     print(q.get())#get是读
#     p.join()


from multiprocessing import Process,Queue
import os,time

def write(q):
    print("启动Write子进程：%s" % os.getpid())
    for i in ['A','B','C','D']:
        q.put(i)#写入队列
        time.sleep(1)
    print("结束Write子进程：%s" % os.getpid())
def read(q):
    print("启动read子进程：%s" % os.getpid())
    while True:#阻塞，等待获取write的值
        value = q.get(True)
        print(value)
    print("结束read子进行：%s" % os.getpid())


if __name__ == '__main__':
    #父进程创建队列，并传递给子进程
    q = Queue()
    pw = Process(target=write,args=(q,))
    pr = Process(target=read,args=(q,))
    pw.start()
    pr.start()

    pw.join()

    #pr进程是一个死循环，无法等待其结束，只能强行结束
    #（写进行结束了，所以读进程也可以结束了）
    pr.terminate()
    print('父进程结束')