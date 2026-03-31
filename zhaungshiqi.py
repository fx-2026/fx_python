
#装饰器带参数，原来的写法上，再套一层函数
from time import ctime,sleep

def outer2(bar):
    def outer(func):
        def inner2(*args,**kwaargs):
            print(func.__name__)
            ret=func(*args,**kwaargs)
            print(bar)
            return ret
        return inner2
    return outer

@outer2('hello')#实际是outer2('hello')foo2()
def foo2(a,b,c):
    # print(a+b+c)
    return a+b+c

print(foo2(1,3,5))
sleep(2)
print(foo2(1,2,3))
print(foo2.__name__)


#wraps和partial的用法