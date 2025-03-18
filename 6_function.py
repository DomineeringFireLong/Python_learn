#define：def funname(parameters):
#函数的第一行成为函数头header,其余部分称作函数体body
#body必须缩进4个空格
#无参函数
def print_hello():
    print("hello python function!")
# print_hello()
#有参函数
def print_string(string):
    print("收到：{}".format(string))
# instr=input("输入字符串：")
# print_string(instr)
def welcome(name,gender):
    if(gender=='male'):
        print("Welcome "+name+' ,please go left')
    else:
        print("Welcome " + name + ' ,please go right')
welcome("Andrew",'male')
welcome("cancy",'female')

#%%函数嵌套定义：在一个函数定义的body里面定义别的函数
def out_fun():
    def inside_fun():
        print("inside_fun has defined!")
    print("out_fun has defined!")
out_fun()#调用外部函数，并不调用内部函数，互不影响
#%%函数参数和函数的返回值
#函数的接口：参数的名字和位置;
# 对于调用者说，fun当作一个黑箱模型即可：知道入口和返回值即可
#参数类型：默认参数、关键字参数、可变参数
#python不像c++，java定义变量有数据类型，所以不支持函数重载
#但可以使用关键字和可变长度参数，也有多态性
# *****************************************
#位置参数
def cal_math(x,y,z):
    return x**2+y*8-z
# 第二个自定义函数覆盖了同名不同参的第一个自定义函数
def cal_math(x,y):
    return x**2+y*8
print(cal_math(1,2))

try:
    cal_math(1,2,3)#报错
except Exception as e:
    print(e)
#%% 关键字参数
def cal(x,y,z):
    print(x**2+y*8-z)
cal(x=5,y=5,z=1)
cal(2,y=5,z=1)
#%%默认值参数
def spam(a,b=6):
    print(a+b)
spam(2)
spam(2,3)
#%%可变长度参数:不仅满足多参数重载，且不用定义多次
#注意区别：*不是地址，而是可变长度
def sum_square(*args):
    sum=0
    for number in args:
        sum+=number**2
    return sum
print(sum_square(1,2,3,4))
list1=[i for i in range(10)]
print(sum_square(*list1))
#%%
#使用双星号**可以将参数收集到一个字典中，参数的名字为字典的键，参数的值是字典的值
#把形参和实参作为键值对生成一个字典
def print_kwargs(**kwargs):
    print('Keyword arguments:',kwargs)
print_kwargs(x=123,y=666,z=686)
# help(print_kwargs)
#%%只接受关键字参数的函数:强制使用关键词参数传递：*参数，或 ,*,后面参数
#本质就是*代表任意位置个元素，所以必须用关键字才能知道是后面的形参
def recv(maxsize,*,block):
    'Receives a message'
    print("test")
    pass
recv(100,block=20)
# help(recv)#里面只要函数名，不需要（）
# recv(100,20)#报错
#%%在 任意多个位置参数的函数中:指定关键字参数：如果不指定，当作前面元素
#注意是任意多个位置，不是迭代器；
def mininum(*values,clip=None):#取最小，但限幅最低值
    m=min(values)
    if clip is not None:#判断元素
        m=clip if clip>m else m
    return m
print(mininum(10,16,66,126,6))
print(mininum(10,16,66,126,6,clip=16))
#传递实参时，进行序列解包
seq_li=[1,2,3,4,5,6]
seq_tup=(1,2,3,4)#元组
seq_dict={1:'a',2:'b',3:'c'}
seq_set={6,6,3}
print(mininum(*seq_li))
print(mininum(*seq_tup))
print(mininum(*seq_dict))
print(mininum(*seq_set))
print(mininum(*range(6,16)))
print(mininum(*map(int,'123')))#map 把str映射成int序列
print(mininum(*zip(range(3),range(3,6))))#zip对象
print(mininum(*(i for i in range(6))))#generator

#%% *本质就是解压：定义多个位置的参数也是个压包解压过程
def myfun(*str):
    print(str)
myfun('put your hands up')# 单星号*把多位置的元素 当作一个 元组
# 双星**用法仅能在函数形参列表用
def myfun1(**fk):
    print(fk)
myfun1(name='bod',age=20,weight=90)# 双星号**生成一个字典:形参：实参
#%%解包问题：*或者**成为序列解包
def demo(a,b,c):
    print(a,b,c)
demo(*(1,2,3))
#  解包的*参数会优先处理,按形参列表ab赋值，而不是按实参的位置
# demo(a=1,*(2,3))#demo() got multiple values for argument 'a'
demo(c=3,*(1,2))#跟赋值顺序无关
# demo(**{'a':1,'b':2},*(3,))#序列解包必须在关键词解包前，报错
# demo(*(3,),**{'a':1,'b':2})#优先处理a报错
demo(*(3,),**{'c':1,'b':2})
# 可变参数之前的参数不能指定参数名，且之后的参数必须指定参数名
def myfun2(a,*b,c=None):
    print(a)
    print(b)
    print(c)
myfun2(1,2,3,4,c=6)#第一个位置为a
# myfun2(a=1,2,3)报错
# 双星号**的可变参数只能放在最后，因为它的实参是关键参数（有形参和实参）
def myfun3(a,*b,c,**d):
    print(a)
    print(b)
    print(c)
    print(d)
myfun3(1,2,3,4,5,6,c=2,m="sadas",n="dvefc")

#函数返回值
def rfun(*args):
    sum=0
    for i in args:
        sum += i
    return sum
rfun(1,2,3,4)
#%%递归调用
def countdown(n):
    if n<=0:
        print('Blastoff')
    else:
        print(n)
        countdown(n-1)
countdown(5)
#函数调用是通过栈的数据结构实现的，调用一次就加一层栈帧，返回时会减一层；
# 无限递归调用会导致栈空间溢出报错

#%%匿名函数
# *********************匿名函数：lambda*****************************
# lambda a,b:a+b
def make_incrementor(n):#用匿名函数可以作为函数生成器
    return lambda x:x+n
f = make_incrementor(12)#给该函数参数，生成个新函数
print(f(1))
print(make_incrementor(12)(12))#从表面看是两个参数：第一个参数给lambda作为其参数，第二个作为输入给函数
#%%
pairs=[(1,'one'),(8,'eight'),(5,'five'),(6,'xin'),(2,'two')]#列表，不是字典
# print(pairs[0][1]) 数列元素为二元，可以当成二维数组提
# print(sorted(pairs,key=lambda i:pairs[0]))#X 比较元素相同，所以没有排序
#用lambda函数提取多为元素的某一维进行排序
print(sorted(pairs,key=lambda i:i[0]))#i是每个pairs的（2元）元素:此处即元组；而字典提的是key
pairs.sort(key=lambda i:i[0])#函数的sort方法调用，不是sorted内置函数用法
print(pairs)
#%%
#*********************map()************************
#fun一个参数，一个数组
li1=[i+1 for i in range(10)]
#对一组数据进行相同运算
def square(x):
    return x*x
li2=list(map(square,li1))#fun,list 函数不加（）和参数
#注意map对象 要用 工厂函数（）生成，不是【】
print(li2)
#fun两个参数，两个数组
def f(x,y):
    return x*y
list_a = list(map(f,[1,2,3],[6,7,8]))
list_b=list(map(f,[1,2,3],[6,7]))
list_c=list(map(f,[1,2],[6,7,8]))
print(list_a)
print(list_b)
print(list_c)
#*************************************变量作用域**************
#%%访问权限取决于变量的赋值域:变量不一定在哪都能访问
# L（local）:局部作用域
# E（enclosing）：闭包函数外的函数中(局部外的局部)
# G（global）：全局作用域
# B(built-in):内建作用域
# 以L->E->G->BS顺序找
x=int(2.9)#内建
g_count = 0#全局
def outer():
    o_c=1#闭包函数外的函数中(函数嵌套定义时)
    def inner():
        i_c=2#局部作用域
        print(i_c)
        print(o_c)#"小范围可以访问大范围"
    # print(i_c)#不能访问
    print(o_c)
# print(o_c)不能访问
print(g_v)
outer()
#只有 模块module、class、def、lambda才会引入新的作用域
#逻辑段不会引入新的作用域:if elif else trp except for while等 #故：代码逻辑段定义的变量外部也可以访问

#%%
total=0
def sum(arg1,arg2):
    total=arg1+arg2
    print('内部total=',total)
#内部会创建同名函数，不会修改外部变量
sum(3,6)
print("外部total",total)
#需要用到global和nonlocal修改
num=1
def fun1():
    "修改外部变量"
#全局变量内部虽然可以访问，但需要加global关键字
    global num
    print(num)
    num=6
    print(num)
fun1()
print(num)
#%%
#修改嵌套作用域
def outer():
    num=10
    def inner():
        nonlocal  num
        print("外部num=",num)
        num=66
    inner()#嵌套的函数，只能在外部函数内部调用
    print("修改后，外部num=",num)
# inner()
outer()


#%%**********生成器***************************
#包含yield关键字的函数就是个生成器函数
#可以把某个变量在循环过程中的值全部保存
def fib(max):
    n,a,b=0,0,1
    while n<max:
        yield b
        a,b=b,a+b
        n=n+1
#yield会暂停、挂起后面的程序，需要不断调用next恢复执行
#生成的是generatoe对象，需要用list（）实例化
print(list(fib(6)))
#%%
def odd():
    print('step 1')
    yield 1
    print('step 2')
    yield 2
    print('step 3')
    yield 3
o=odd()
#%%************************协程*******************
#generatoe是数据的生产者，协程是数据的消费者


