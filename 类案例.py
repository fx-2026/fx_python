
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

#网络上的案例
class Human:
    # 这是一个“类属性”，相当于工厂的默认设置
    default_name = "无名氏"

    def __init__(self, name):
        self.name = name

    # --- 这是一个普通方法 ---
    def say_hello(self):
        # 只有具体的人才能打招呼
        print(f"你好，我是 {self.name}")

    # --- 这是一个类方法 ---
    @classmethod
    def change_default_name(cls, new_name):
        # cls 代表的是 Human 这个类（工厂），而不是某个人
        cls.default_name = new_name
        print(f"工厂设置已修改！现在的默认名字是：{cls.default_name}")

# ================= 运行开始 =================

# 1. 使用类方法（直接找工厂改设置）
# 注意：不需要造人，直接通过类名调用
Human.change_default_name("张三") 

# 2. 造两个人
p1 = Human("小明")
p2 = Human("小红")

# 3. 看看效果
# 虽然 p1 和 p2 的名字是自己定的，但如果他们没名字时，
# 就会用到工厂刚才改过的默认设置。
print(f"工厂现在的默认设置是：{Human.default_name}") 



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



#限制传入的类型和范围装饰器（整数，且满足18-65）
print('*'*30+'限制传入的类型和范围装饰器（整数，且满足18-65）'+'*'*30)

class Age(object):
    def __init__(self,default_age = 18):
        self.age_range = range(18,66)
        self.default_age=default_age
        self.data ={}

    def __get__(self,instance,owner):
        return self.data.get(instance,self.default_age)
    
    def __set__(self,isinstance,value):
        if value not in self.age_range:
            raise ValueError('must be in (18-65)')
        
        self.data[isinstance]= value

class Student(object):
    age =Age()


if __name__=='__main__':
    s1 = Student()
    s1.age =30
    s1.age =20
    print(s1.age)
    #s1.age =100

#固定部分参数


#获取当前的状态

@property
def current_state(self):
    instance_state ={
        1:'运行',
        2:'离线',
        3:'下线'
    }

    if (time_diff.seconds)>=300:
        return instance_state[2]

    if self.state in range(10):
        return instance_state.get(self.state,'其他')
    return None

#cloud.vpc.0001.current_state 

#类里面将方法改成属性，这样可以直接输出
#描述的协议__get__,__set__,__delete__
#__getattr__,__setattr__,__delattr__,__getattribute__,property,staticmethod,classmethod通过上层协议做的不同的封装
#property将类里的方法，函数变成属性，传self
#classmethod将实例的方法变成类的方法，传cls
#staticmethod将类外面的方法，改成类里面的方法，（）什么都不传
