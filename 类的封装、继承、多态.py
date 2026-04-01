#类的封装，将类封装成对象

#type\list\dict\people的父类都是object
#list\object\dict\people都是type的实例，type也是type的实例
#谁创建了谁就是实例化


#多重继承问题
#一个子类可以继承多个父类
#多个父类，继承顺序问题，钻石继承，

print('*'*30+'钻石继承问题'+'*'*30)

class BaseClass(object):
    num_base_calls=0
    def call_me(self):
        print("Calling method on Base Class")
        self.num_base_calls +=1

class LeftSubclass(BaseClass):
    num_left_calls = 0
    def call_me(self):
        print("Calling method on Left Subclass")
        self.num_left_calls +=1

class RightSubclass(object):
    num_right_calls = 0
    def call_me(self):
        print("Calling method on Right Subclass")
        self.num_right_calls +=1

class Subclass(LeftSubclass,RightSubclass):
    pass

a =Subclass()
a.call_me()

b =RightSubclass()
b.call_me()
print(Subclass.mro())#查看继承顺序




#工厂模式，传入不同的数据调用不同的类，出现不同的值
print('*'*30+'工厂模式，传入不同的数据调用不同的类，出现不同的值'+'*'*30)
class Human(object):
    def __init__(self):
        self.name = None
        self.gender = None
    def Getname(self):
        return self.name
    
    def Getgender(self):
        return self.gender

class Man(Human):
    def __init__(self,name):
        print (f'This is man name {self.name}')

class Woman(Human):
    def __init__(self,name):
        print (f'This is woman name {self.name}')


class Factory():
    def __init__(self):
        self.name = None
        self.gender = None
    def getPerson(self,name,gender):
        # print(name,gender)
        if self.gender == 'M':
            return Man(name)
        elif self.gender == 'F':
            return Woman(name)
        else:
            pass

if __name__ =='__main__':
    factory =Factory()
    factory.getPerson('Stephen','M')