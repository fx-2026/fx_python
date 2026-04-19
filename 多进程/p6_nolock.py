#进程锁lock
#不加进程锁
#让我们看看没有加进程锁时会产生什么样的结果。


import multiprocessing as mp
import time

def job(v,num):
    for _ in range(5):
        time.sleep(0.1)#暂停0.1秒,让输出效果更明显
        v.value += num#v.value获取共享变量值
        print(v.value,end="|")


def multicore():
    v = mp.Value('i', 0)  # 定义共享变量
    #typecode_or_type: 一个字符代码，用于指定C语言中的数据类型，例如
    #'i'代表整数(int)，
    #'d'代表双精度浮点数(double)，
    #'c'代表字符串
    p1 = mp.Process(target=job,args=(v,1))
    p2 = mp.Process(target=job,args=(v,3))#设定不同的number看如何抢夺内存
    p1.start()
    p2.start()
    p1.join()
    p2.join()

if __name__ == "__main__":
    multicore()

#在上面的代码中，我们定义了一个共享变量V，两个进程都可以对它进行操作。
#在job()中我们想让V每隔0.1秒输出一次累加num的结果，
#但是在两个进程P1和p2中设定了不同累加值。
#所以接下来让我们来看下这两个进程是否会出现冲突
