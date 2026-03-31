from functools import wraps
#wraps 的作用就是：把原函数的信息“复制”给包装后的函数，让装饰后的函数看起来还是原来的那个函数。

#日志打印案例
from datetime import datetime, timedelta
def logit(logfile = 'out.log'):
    def logging_decorator(func):
        @wraps(func)
        def wrapped_function(*args,**kwargs):
            # 1. 获取当前日期，并替换时间部分为 00:00:00
            today_midnight = datetime.now().replace(hour=0, minute=0, second=0, microsecond=0)

            # # 2. 格式化为 'yyyymmdd 00:00:00' 字符串
            # formatted_time = today_midnight.strftime("%Y%m%d 00:00:00") 
            log_string =func.__name__ +" was called " +str(today_midnight)
            print(log_string)
            with open(logfile,'a') as opened_file:
                opened_file.write(log_string+'\n')
                return func(*args,**kwargs)
        return wrapped_function
    return logging_decorator



@logit()
def do_work(*args,**kwargs):
    pass

do_work()
#@functools.lru_cache它的核心作用是自动缓存函数的执行结果，避免对相同参数的重复计算，从而显著提升程序性能。
#lru_cache 最经典的用法是优化递归算法，例如计算斐波那契数列。没有缓存的递归会进行大量重复计算，效率极低。
import functools 
@functools.lru_cache()
def fibonacci(n):
    if n<2:
        return n
    return fibonacci(n-2) + fibonacci(n-1)
if __name__=='__main__':
    import timeit
    print(timeit.timeit("fibonacci(12)",setup="from __main__ import fibonacci"))