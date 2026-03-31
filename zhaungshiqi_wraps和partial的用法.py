from functools import wraps
#wraps 的作用就是：把原函数的信息“复制”给包装后的函数，让装饰后的函数看起来还是原来的那个函数。
def my_decorator(func):
    @wraps(func)  # 加上这一行，原函数的元数据就被保留了
    def wrapper(*args, **kwargs):
        return func(*args, **kwargs)
    return wrapper

@my_decorator
def add(a, b):
    """这是一个加法函数"""
    return a + b

print(add.__name__)  # 输出: add (正确！)
print(add.__doc__)   # 输出: 这是一个加法函数 (正确！)


