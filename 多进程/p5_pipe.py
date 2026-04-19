#管道
#官方文档
#pipe()函数返回一个由管道连接的连接对象，默认情况写是双工（双向）

from multiprocessing import Process,Pipe
def f(conn):
    conn.send([42,None,'hello'])

if __name__ == '__main__':
    parent_conn,chiled_conn = Pipe()
    p = Process(target=f,args=(chiled_conn,))
    p.start()
    print(parent_conn.recv())
    p.join()



#返回的两个连接对象 Pipe() 表示管道的两端。
#每个连接对象都有 send() 和 recv()方式（相互之间的）。
#请注意，如果两个进程（或线程）同时尝试读取或写入管道的同一端，
#则管道中的数据可以会损坏。当然，同时使用管道的不同端的进程不存在损坏的风险。



#队列和管道都是先进先出
#队列可以排成几列
#管道连接两头