#不同的命名空间可以定义相同的类
#作用域和闭包机制：local、enclosing、global、built-in内置
#函数、类、lambda函数定义的命名变成局部作用域的命名：会覆盖全局变量，但该域外这些局部变量就失效了
#而循环、条件、顺序语句的作用域是全局

# def outer_func(a):
#     num = 10
#     def inner_func(b):
#         nonlocal num#直接访问闭包变量
#         print("访问外部变量num="+str(num))
#         print("a="+a+"  b="+b)#外层函数内层的闭包,a为内部函数的闭包函数，外部函数执行完毕后，变量a仍存在
#     return inner_func#外部函数返回的时内部函数
#
# example =outer_func("100")
# example("66")

#%%*************装饰器*******************************
#更广义的装饰：用函数或类生成
# 功能：不改变原有代码的基础上增添新的功能属性：常用于程序日志记录，性能测试、权限校验等场景
#自定义一个装饰器
# def start_logging(func):
#     def wrapper():#包装
#         # name是函数的内置函数
#         print(func.__name__+" is running")#在原来的函数前面加一句功能
#         return func()#调用原来的函数
#         print(func.__name__ + " has done")#不执行之后的语句
#     return wrapper
# # def demo():
# #     print("this is demo ")
# # d=start_logging(demo)#加一层装饰生成函数
# # d()#d是wrapper函数名
#
# #更简洁的使用方法
# @start_logging# 装饰器函数
# def demo():#逻辑业务函数
#     print("this is demo ")
# demo()
#参数的处理，若逻辑业务函数需要传递外部参数，wrapper（）需要加*args，**kkwargs

# def start_logging(func):
#     #任何多个无名参数 tuple;关键字参数dict;同时使用*args和**kwargs时，必须*args参数列要在**kwargs前
#     def wrapper(*args,**kwargs):#普通参数和关键字参数，前者元组、后者字典
#         print(func.__name__+" is running! ")
#         return func(*args,**kwargs)#也可以不加,**kwargs
#     return wrapper
# @start_logging
# def demo2(arg1,arg2):
#     print("this is a "+arg1+arg2)
# demo2("demo2","  haha!")

#多级修饰，装饰器参数
# def log(content):
#     def decorate(func):
#         def wrapper(*args,**kwargs):
#             print("decorate :"+content)#内部可调用外部变量
#             print("wrapper :"+func.__name__)
#             return func(*args,**kwargs)
#         return wrapper
#     return decorate
# @log("zhangdapao_add")
# def add(x,y):
#     return x+y
# print(add(10,26))
# help(property)只能看到方法，但最底层的c语言是看不到的

#********调用顺序**************
#一个函数可以用多个装饰器装饰，从内往外的顺序
# def a(funca):
#     print("a is running")
#     def wrapper():
#         print(funca.__name__+" is running")
#         return funca
#     return wrapper
# def b(funcb):
#     print("b is running")
#     def wrapper():
#         print(funcb.__name__+" is running")
#         return funcb
#     return wrapper
#
# def c(funcc):
#     print("c is running")
#     def wrapper():
#         print(funcc.__name__+" is running")
#         return funcc
#     return wrapper
# @a
# @b
# @c
# def fund():
#     print("fund is running")
#
# fund()#等价于f=a(b(c(fund)))#先进行最内层


#module
#代码量大的程序：用文本编辑器或集成开发环境.py脚本：可以拆成多个脚本文件，就成为模块

#标准库（自带模块）直接导入
# import math
# print(math.cos(math.pi))
#也可以只导入指定的函数或方法
# from math import cos
# from math import pi
# print(cos(pi))

# from math import *#隐式导入，不推荐，未知变量和方法不一定与当前脚本得到变量和方法重合，未知后果
# print(cos(pi))

#可以导入自定义模块：涉及到模块搜索路径；
# 可通过sys.path查看模块搜索路径
# import sys
# import pprint
# pprint.pprint(sys.path)#E:\\Anaconda\\anaconda\\lib\\site-packages'模块的路径
#
# import somemodule #将整个模块导入
# from somemodule import somefunction#从某个模块导入某个函数
# from somemodule import firstfun,secondfun,thirdfun#多个函数
# from somemodule import * #某个模块的全部函数导入

#************************* 包 ************************
#import 导入包时，解释器只导入__init__.py文件，该文件中导入什么模块、定义什么函数、什么变量都会导入

#包管理工具 pip
# pip --version #查看版本和路径
# pip --help
# pip install -U pip 升级pip
# pip install xxx
# pip install xxx-2.1.0
# pip install xxx>=1.0.5
# pip install --upgrade xxx#更新库
# pip uninstall xxx
# pip show#显示已安装库的信息
# pip show -f xxx#查询该库的信息
# pip list#列出已安装的库
# pip list -o#列出可升级的库
# pip freeze#已安装的库和版本信息
# pip install xxx -i http:// .. #按路径进行安装
# pip install -r requirements.txt #安装指定文件的库 ++ >= <+指定版本;requirements.txt内容为 APScheduler==2.21 ...
# python3 -m pip install xxx#当python2和3都有pip时，安装在3中

#区别：
#1.模块，英文为Modules，本质上是一个Python程序，以.py作为文件后缀。任何py文件都可以作为一个模块。
# 通过使用模块，可以有效地避免命名空间的冲突，可以隐藏代码细节让我们专注于高层的逻辑，还可以将一个较大的程序分为多个文件，提升代码的可维护性和可重用性。
#在完成一个模块的编写之前，我们一般会对模块中的功能进行测试：if __name__ == '__main__':

#2.包（package）来管理这些模块。
# Python包，就是里面装了一个__init__.py文件的文件夹。
# 它本身是一个模块，这个模块的模块名不是__init__，而是这个包的名字，也就是装着__init__.py文件的文件夹的名字。
# 作用是将一个文件夹变为一个Python模块
# 在这个包被import的时候，这些代码会自动被执行
# __all__是Python中的一个重要的变量，放在__init__模块中，用于指定此包（package）被import *时，哪些模块（module）会被import进当前作用域中
# 不在 __all__列表中的模块不会被其他程序引用。我们可以对 __all__进行重写
# __path__也是python中的一个常用变量，它是储存着当前包内的搜索路径的一个列表。默认情况下只有一个元素，即当前包（package）的路径。


#3.库只是一个通俗的说法，既可以是一个模块也可以是一个包：
# 我们常用的os库、random库、re库都在里面，这些“库”都是一个个的python文件即模块；
# 而json、collections、sqlite3还有tkinter这些“库”又是一个一个的文件夹（里面都有__init__.py)也就是包


# 当哪个模块被直接执行时，该模块“__name__”的值就是“__main__”
# 当被导入另一模块(py文件)时，“__name__”的值就是模块的真实名称
# if __name__ == '__main__': 该语句的作用就是，只当运行该程序时运行之后的程序，别的程序调用该模块时不执行；
# 程序执行顺序仍然是从上往下，与c++的main不一样






