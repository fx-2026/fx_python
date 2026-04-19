import os
import threading
import time
from multiprocessing import Process

class MyThread(threading.Thread):#继承Process创建新的类
    def __init__(self,num):

        super(MyThread,self).__init__()
        self.num = num

    def run(self):#重写Process类中的run方法

        print("current",self.num)

if __name__ == '__main__':
    t1 =MyThread("thread 1")
    t2 = MyThread("thread 2")
    t1.start()
    t2.start()
    t1.join()
    t2.join()

