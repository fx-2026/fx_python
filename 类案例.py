
#将方法封装成属性
print('*'*30+'将方法封装成属性'+'*'*30)
class Human2(object):
    def __init__(self):
        self._gender = 'N'

    @property #将方法封装成属性
    def gender2(self):
        print(self._gender)

    #支持修改
    @gender2.setter
    def gender2(self,value):
        self._gender = value

    #支持删除
    @gender2.deleter
    def gender2(self):
        del self._gender

h = Human2()
h.gender2
h.gender2 = 'F'
h.gender2
del h.gender2

#另一种property写法
#gender = property(get_,set_,del_,'other property')不推荐


#让实例的方法变成类的方法
print('*'*30+'让实例的方法变成类的方法'+'*'*30)
class A (object):
    bar = 1
    def foo(self):
        print('in foo')

    #使用类属性方法
    @classmethod
    def class_foo(cls):#cls是类
        print(cls.bar)#打印类的属性
        cls().foo()#调用类的方法

A.class_foo()

#案例2
print('*'*30+'让实例的方法变成类的方法，案例2'+'*'*30)

class Story(object):
    snake = 'Python'
    def __init__(self,name):
        self.name =name

    #类的方法
    @classmethod
    def get_apple_to_eve(cls):
        return cls.snake


if __name__ == '__main__':
    s = Story('anyone')
    #get_apply_to_eve 是 bound方法，查找顺序是先找到s的__dict__是否有get_apple_to_eve,如果没有，
    print(s.get_apple_to_eve)
    # #类和实例都可以使用
    print(s.get_apple_to_eve())
    print(Story.get_apple_to_eve())
    print(type(s).__dict__['get_apple_to_eve'].__get__(s,type(s)))
    print(type(s).__dict__['get_apple_to_eve'].__get__(s,type(s)) == s.get_apple_to_eve)#实例的属性和类的属性一样
    #s是对象，type(s) 是取得s的类，__dict__['get_apple_to_eve']，取得类的默认属性和方法，通过get协议在进行操作取得实例


#静态的方法
print('*'*30+'静态的方法'+'*'*30)
import datetime
class Story(object):
    snake = 'Python'
    def __init__(self,name):
        self.name =name
    #静态方法
    @staticmethod
    def god_come_go():
        if datetime.datetime.now().month % 2:
            print('god is comming')

Story.god_come_go()

#静态方法可以由类直接调用
#因为不传入self也不传入cls,所以不能使用类的属性和实例的属性