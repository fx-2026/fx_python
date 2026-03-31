
print('*'*30+'类的装饰器的用法'+'*'*30)
def decorator(aClass):
    class newClass(object):
        def __init__(self,arg):
            self.times = 0
            self.wrapped = aClass(arg)#将num这个类代入到wrapped这个实例
        
        def display(self):
            self.times +=1
            print("run time",self.times)
            self.wrapped.display() #调用num,中的display方法
    return newClass



@decorator#装饰器作用，将num中display的方法替换成装饰器的方法    
class num(object):
    def __init__(self,number):
        self.number =number

    def display(self):
        print("number is",self.number)


x = num(6)
for i in range(5):
    x.display()




#装饰器的其他用法
print('*'*30+'1、向函数添加一个属性'+'*'*30)
#1、向函数添加一个属性
def attrs(**kwds):
    def decorate(f):
        for k in kwds:
            setattr(f,k,kwds[k])
        return f
    return decorate

@attrs(versionadded="2.2",
       author ="guido van rossum")
def mymethod(f):
    pass

print (mymethod.versionadded,mymethod.author)



#函数参数观察器
print('*'*30+'函数参数观察器'+'*'*30)
import functools

def trace(f):
    @functools.wraps(f)
    def decorated_function(*args,**kwargs):
        print(f,args,kwargs)
        result = f(*args,**kwargs)
        print(result)
    return decorated_function


@trace

def greet(greeting,name):
    return '{},{}!'.format(greeting ,name)

greet('better','me')

#用单实例定义一个类
print('*'*30+'用单实例定义一个类'+'*'*30)

def singleton(cls):
    instances={}
    def getinstance():
        if cls not in instances:
            instances[cls] =cls()
        return instances[cls]
    return getinstance

@singleton
class MyClass:
    def __init__(self):
        # self.name =name
        # self.rise =rise
        print('你好')
    
    # def goods(self):
    #     y = self.name
    #     x = self.rise
    #     return "name:" +y + " goods:" + x

# x =MyClass('Tom','rise').goods()
# print(x)
x =MyClass()



#类的相等判断，简化
print('*'*30+'类的相等判断，简化装饰器'+'*'*30)


#原始不带装饰器写法
print('*'*30+'原始不带装饰器写法'+'*'*30)
class Xclass():
    def __init__(self,var_a,var_b):
        self.var_a=var_a
        self.var_b =var_b
    def __eq__(self,other):
        if self.__class__ is not other.__class__:
            return False
        return (self.var_a,self.var_b) == (other.var_a,other.var_b)


var_1 = Xclass(1,2)
var_2 = Xclass(1,2)
print(bool(var_1 == var_2))


#带装饰器写法
print('*'*30+'带装饰器写法'+'*'*30)

from dataclasses import dataclass
@dataclass
class Yclass():
    var_a:str
    var_b:str

 
var_3 = Xclass(1,2)
var_4 = Xclass(1,2)
print(bool(var_3 == var_4))