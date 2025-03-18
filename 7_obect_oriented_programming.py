#封装；继承、多态
#类可以定在一个函数内部或者if语句下
# 成员函数有参数self:self是实例对象，就是c++中this指针，指向内部成员属性
# 类有object参数：oeject是所有类的基类，继承基类中的所有方法
# class classname(object):
#     name =  'xiaohuolong'
#     card = "20231006"
#     __score= 100#私有成员
#     def __init__(self,n1,c1,s1):
#         self.name = n1
#         self.card = c1
#         self.__srore= s1
#         #属性也可以直接初始化,不用定义
#         self.value=100
#         # print(self)#class object 的地址
# c1=classname("penhuolong","3220221006",100)
# c1.addatt="外部加一个属性"
# # print(c1.score)#会报错
# #私有成员：__name  访问 对象名._类名__属性名
# print(c1._classname__score)#私有成员可以访问只是更麻烦了，但不能阻止
# print(c1.addatt)
# # print(c1.name)
#%%类的属性可以动态添加、删除、修改
#派生类、多重继承、运算符重载
#派生类继承了父类（基类）的成员函数，但也可以重写，也可继承和修改基类的属性
# class base:#不继承时，不用（）
#     #也可以继承object
#     name='base'
#     sex='male'
#     def value(self):#成员函数自带self
#         return "300"
#
# class base2(object):
#     def say(self):
#         print("Hello")
# #多重继承:一个类同时继承多个基类
# class derived(base,base2):
#     def value(self):#成员函数自带self
#         return "600"
#     name='derived'
#     sex='female'
# c2= base()
# c3= derived()
# print(c3.value())
# c3.say()
#%% 函数虽然不能重载
# 运算符重载(其实还是成员函数)：在类的方法中定义了同名的方法（拦截了内置方法）
# class cz:
#     def __init__(self,start):
#         self.data=start
#     def __sub__(self, other):
#         # return cz(self.data-other)#结果生成一个类，而不是数
#         return self.data-other #直接数方便
#
#     def __abs__(self):
#         # return cz(self.data*-1)#结果生成一个类
#         return self.data * -1
# a=cz(66)
# print(a.data)
# #任何的与类a运算的结果生成一个a类
# print(a-60)#sub与-运算符重载
# print(abs(a))#把abs改成了取反

#%%***********************新式类*************************************
#经典类什么都不继承，3.0版本之后的python新式类都继承于object，有内置方法和属性
#新式类有__dict__属性，把对象的属性用字典存储；可以自定义__slot__序列类型的对象（列表，元组或其他迭代对象），节省内存
# class xsl(object):
#     a="123"
#     b=123
#
# class xsl_s(object):
#     #利用这种方法可以实现私有属性
#     b = 222#read-only
#     __slots__ = ['a','c']#这样的话，可以修改外slot变量；外部不能随意的定义其他属性；且非slot属性只读
#
#
# l1=xsl()#定义对象时，类（）
# l2=xsl_s()
# l2.a=111
# # l2.b=222 #外部不能更改
# l2.a=123
# l2.c=666
# # print(xsl.__dict__)
# print(l2.__slots__)
#C++是静态编译性语言，不能在外边随意给对象加属性
#python是动态解释性语言，必须加入 数据类型检查代码 才可以防止引用类型错误
#若一个类修改了__get__ __set__ __del__一个及以上 则该类为描述符（其实例对象通常是另一个类的属性）:把描述符类作为另一个类的属性
# class TheString(object):
#     def __init__(self):
#         self.__name="Default string"#私有成员
#     def __get__(self, instance, owner):# 访问实例对象会返回值 .object
#         return self.__name
#     def __set__(self, instance, value):#外部修改对象参数时,调用 obkect=
#         if type(value) is str:
#             self.__name=value
#         else:
#             raise TypeError(str(value)+" is not a string")
#
# class Classname(object):
#     value=TheString()
#     card=123
#     def __getattr__(self, item):
#         return "not default attr"
#     # def __getattribute__(self, item):#访问实例属性时无条件调用，正常的属性也会进入该方法
# cc=Classname()
# print("value="+cc.value)#这样的话修改value就必须是字符串
# #***如果对象找不到属性就会发生AttributeError报错,可以通过自定义__getattr__()方法，避免程序抛出异常中断程序
# cc.vv=123#动态赋予属性是可以的
# print(cc.dfas)#但访问未定义属性不会报错
#%%**************************装饰器**************************
#@property 作用：让对象的方法看上去像属性：把函数作为属性访问
# class zsq(object):
#     @property#特性、属性
#     def value(self):
#         return "100"
#     #每个函数前面加装饰器，则必须用属性访问方法，就是不加（）
#     @property  # 特性、属性
#     def say(self):
#         return 'hello'
# zsq1=zsq()
# print(zsq1.say())
# print(zsq1.say)#不加装饰器时候返回函数地址
# print(zsq1.value)

# class classname(object):
#     def __init__(self):
#         self.v=100
#     @property
#     def value(self):
#         return self.v
#     @value.setter
#     def value(self,value):
#         print("修改v值="+str(value))#TypeError print里面的数据必须都是str
#         self.v=value
#     @value.deleter
#     def value(self):
#         print("删除v值")
#         del self.v
#
# c_=classname()
# print("value=",c_.value)
# c_.value=666#调用setter
# del c_.value#调用deleter

#%%*******类设计技巧***********
#1.调用基类的方法，super()方法
# class basec():
#     def print(self):
#         print("baseclass_print")
# class deric(basec):
#     def print(self):
#         super().print()#基类方法
#         print("derived class print")
#
# de=deric()
# de.print()
#*******************
# 静态方法和类方法区别
#实例对象的方法只能被实例对象调用，而@stasticmethod修饰的静态方法和@claamethod类方法可以被类和实例对象调用
# class sc():
#     def __init__(self):
#         self.data="100"
#     @staticmethod
#     def out_data(object_,name):#不需要self
#         print(str(name)+" : "+object_.data)
#     @classmethod
#     def cm(cls,data):#不需要self，第一个参数传类名进去
#         c_=cls()#在方法里面创建一个类
#         c_.data=data
#         return c_#创建一个对象;用于对对象重新构造赋值
#
# a=sc()
# sc.out_data(a,"xkl")#静态方法的调用：类.方法（对象，其他参数） 通过类名调用
# #利用类方法可以创建一个对象
# c2=sc.cm("200")#类方法调用：类.方法（其他参数），也是通过类名调用,注意不需要在第一个参数加类名了
# print(c2.data)
# #类方法提供了重构对象的灵活性，不需要修改构造函数（初始化）
# a=sc.cm("500")#重构a对象
# sc.out_data(a,'phl')
#%%*********创建大量对象时减少内存占用：利用__slot__特性，作为简单的数据结构

class Date_store():
    #内存优化和局限的封装性
    __slots__ = ['year','month','day']#用列表存储属性，且外部不可以添加属性,也不支持多重继承
    def __init__(self,year=2023,month=11,day=21):#带默认参数的拷贝构造函数
        self.year=year
        self.month=month
        self.day=day

date=Date_store(2023,11,22)
print(date.__slots__)#外部可以删除属性的实参，但是slot中的形参还是存在的

