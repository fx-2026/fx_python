import requests
from multiprocessing.dummy import Pool as ThreadPool

urls =['http://www.baidu.com',
       'http://www.163.com',
        'http://www.qq.com',
       'http://www.taobao.com']

#开启线程池
pool = ThreadPool(4)
#获取urls的结果
result =pool.map(requests.get,urls)
#关闭线程池等待任务退出
pool.close()
pool.join()
for i in result:
    print(i.url)