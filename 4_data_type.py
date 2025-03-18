import copy
import math
#解压序列赋值给多个变量
tuple1=(6,8,(6,6,6))
x,y,z=tuple1
print(x,y,z)
print(x,y,z[1])
#工厂函数list(),tuple(),set(),dict()
#python会调用 垃圾回收机制，释放内存
# del sequence 当不用该数据对象时，删除整个对象;对于可变序列的对象可以删去部分元素

#%%
#*****************************list**********************************
#特点：
#1.有序集合、2.索引从0开始、3.正向索引起始和末尾元素序号为 0 到 n-1、4.负向索引起始和末尾元素序号-n,-1 反向从-1开始减
#第i个元素， i-1 或者 i-1-n=-(n-i+1)
list1=[]
list2=[1,2,1,2,1,2,4,1]
for i in range(10):
    list1.append(i+1)
list1.extend(list1)#等价于 +=  不能用append,否则会被当作一个元素(列表)
print(list1)
print(list1[-2])
print(list1.index(3))#返回第一个为3的索引号
print(list1.count(6))#返回为6的值的个数
list1.insert(2,"xkl")
list1.remove(3)#删除第一次出现的元素
print(list1.pop(8))#删除并返回该索引号（参数）的元素
print(list1)
list1.clear()
print(list1)
del list1,list2
#%%
#*********************列表作栈*************************
stack=[3,4,5]
stack.append(6)#入栈，后入先出
print(stack.pop())#出栈
#%%
# *******************常用内置函数***************************
list3=[1,12,124,15,131,123,230]
print(max(list3))
print(min(list3))
print(len(list3))
print(sum(list3))
list4=[3,25,54,12,64,12,-12]
# li=zip(list3,list4)#元组组成的列表
li=zip(*zip(list3,list4))#这种方式，解压后的列表可单独分开为两个元组
x,y=list(li)#由数据的地址直接生成列表
print(li)
print(list(li))#元组为元素的列表
print(x,y)
del li

#%%
#******************enumerate常与for循环使用，可以用于计数
seasons=['spring','summer','fall','winter']
seq=list(enumerate(seasons,start=1))
for i,element in enumerate(seasons):
    print(i+1,element)

for i, element in seq:
    print(i, element)
#%%
# ***成员资格判断
classmate1=['james','hadon','shark']
print('shark' in classmate1)
print('andon' in classmate1)
#%%%切片操作:从列表中取部分元素
classmate2=['james','hadon','shark','bob','andrew','lebron','xkl']
#[:2] 0 1 没有2; 起：终：间隔
print(classmate2[::3])
print(classmate2[:-1])
#%%列表索引
list5=[3,25,54,12,64,12,-12]
# list5.sort()#改变原对象，不返回副本
sot=sorted(list5)#返回一个副本，不对原对象修改
print(list5)#不能直接调用函数并打印
print(sot)
# list5.reverse()#不返回列表，直接修改
res=list(reversed(list5))#地址转化为列表
print(res)

#%%
#复制问题
cp_list=[3,[2,1,2],7,9,11,1]
cp1=cp_list.copy()
cp2=copy.deepcopy(cp_list)
cp_list[0]=6
print(cp1)
print(cp2)
cp_list[1][2]=6
print(cp1)
print(cp2)

#%%
#*************************列表推导式***************
list6=[(i+1)**2 for i in range(12) if i%2==0]
print(list6)

#**********************list_end*******************************************
#**********************tuple***********************************************
#%%
t1=tuple('asbdjhbda')#自动把字符串元素变成单个元素
t2=('afds',)#元组一个元素尽量加逗号，否则不是元组数据,而被认为是字符串
l1=[1,2,3,4,5,6]
t3=tuple(l1)
t4=1,2,3,4,5,6#实际上根据逗号识别元组，而不是()
print(t1)
print(t2)
print(t3)
print(t4)
#%%
#The difference between list and tuple
# 1.不能修改，无append,extend,insert,remove,pop
# 2.占用内存少，速度快
# 3.不能修改，安全性高
# 4.元组可用作字典键、集合元素（列表不可）
# 5.利用list()，tuple()，两者可以相互转换
# ***********************tuple_end****************************
#%%
#***********************sequence unpacking**********************
# 序列解包：对多个变量同时赋值；对象：列表、字典的键、enumerate、filter对象等
# 本质把一个序列/可迭代对象的多个变量进行同时赋值；
# a,b,c=['a','b','d']
# print(a)
# a,b,c=enumerate(['a','b','d'])
# print(a)
# a,b,c=('a','b','d')#tuple
# print(a)
# a,b,c={'a':1,'b':2,'d':3}#dictionary
# print(a)
# a,b,c='abc'#string
# print(a)
# a,b,c=[x+1 for x in range(3)]#生成器 生成列表
# # d=tuple(x+1 for x in range(3))#generator 生成器对象：地址形式
# d=tuple(x+1 for x in range(3))#可以加上工厂函数变成对象
# print(a,b,c)
# print(d)
# # x,y,z=iter([1,2,3])
# x,y,z=map(str,range(3))#从0-2的字符
# print(y)
x[:] = map(str,range(5))#把列表的0元素换成0-4序列，不等长交换
print(x)
#%%压包是解包的逆过程zip
# a=['a','b','c']# b=[1,2,3] low
a=tuple("abcdefg")#元组可以对字符串直接生成
a=list(a)
b=[i+1 for i in range(7)]#列表可以对generator直接生成
c=[7-i-1 for i in range(7)]#列表可以对generator直接生成
# print(a)
# print(b)
# for i in zip(a,b):#i为元组
#     print(i)
for i,j in zip(b,c):
    print("{}+{} = {}".format(i,j,i+j))
#%% *符号参数
#调用函数时，实参前面加一个*可以进行序列解包：把序列值传递给形参
ls=[('james','2000-8-1',24,'male'),('marry','20001-11-12',23,'female')]
# for name,*arg,sex in ls:#*arg 代表一个序列对象，可以提取多个参数
#     print(name,arg,sex)
# 单个元素不用时，用下划线_占位，多个元素不用时，用*_占位
for name,*_,arg in ls:#*arg 代表一个序列对象，可以提取多个参数
    print(name,arg)
#%%********generator expression 生成器推导式************************
#列表推导式：
g1=[10-abs(i) for i in range(-5,6)]
#生成器推导式:生成的是生成器对象，不能直接访问，用list或者tuple函数转换
g2=(10-abs(i) for i in range(-5,6))
# #tuple没有直接的推导式，用生成器推导式生成再改对象类型
# g2=tuple(g2)

g2.__next__()#generator对象的方法
next(g2)#内置函数
# 循环迭代
for i in g2:
    print(i)
print(list(g2))
#生成器对象是一次性的，不能重复迭代，所有元素访问完后，为空

#***************************************dictional***************************
#%%字典：映射的数据结构：元素为key-value对，又称item条目。键唯一，但值可重复;可修改
# #create
# # d2=dict()
# one_dict={
#     'apple1':'good',
#     'apple2':'small',
#     'apple3':'not good'}
# #increase element
# one_dict['banan']='good'
# print(one_dict)
# d2=dict([(1,90),(2,92),(3,88)])
#双元素序列：嵌套元组的列表，或者列表的元组，列表的列表等等都可以转换字典
# d2[5]=100
# print(d2)
#********把两个序列转换成字典
x=[i+1 for i in range(5)]
y=[math.cos(i) for i in range(5)]
d3=zip(x,y)
dict(d3)
#%%****
#键是不可变数据(只能用整数、字符串、元组等不可变数据)，不允许重复；
# 值是可变(故可以采用列表、集合、字典)等可变数据；可重复、不唯一
#通过键获得值。不能反过来
#访问 字典名[key]
dict1={
    'apple1':'good',
    'apple2':'small',
    'apple3':'not good'}
print(dict1.keys())
print(dict1.values())
print(dict1.items())
# print(dict1['apple1'])
# 通过外部访问字典小程序
# get = input("请输入查找对象名")
# if get in dict1:
#     # print(dict1['apple5'])#没有该key 会报错，增加robust可以先in判断
#     print(dict1[get])  # 没有该key 会报错，增加robust可以先in判断
# else:
#     print("can not fine the element")
# #get方法，用于增加robust，防止找不到key报错
# print(dict1.get('apple2'))
# print(dict1.get('apple5'))#默认返回None
# print(dict1.get('apple6','can not find!'))#修改默认返回
#%%
#统计词频
sentence="Life is short,we need python"
counts={}
for c in sentence:
    #如果字符是c 就在字典key=c的位置，原来的value加1；若还没出现过字符c，则先给0再+1
    counts[c]=counts.get(c,0)+1
print(counts)

#%%%
dict1={
    'apple1':'good',
    'apple2':'small',
    'apple3':'not good'}
#修改值
dict1['apple1']='very delicious!!'
#合并两个字典update
dict2={
    'apple3':'well',
    'apple4':'very big',
    'apple5':'a little bad'
}
dict1.update(dict2)#重复，后面代替前面
del dict1['apple4']#删除
dict1.pop('apple5')#删除
dict2.clear()#删完
print(dict1.items())
print(dict2.items())
#%%有序字典
from collections import OrderedDict
d=OrderedDict()#内部多一个维护的双向链表，内存大
#普通字典是无序的键值对
no_d={'a':3,'b':2,'z':1}
d['foo']=1
d['bar']=2
d['spam']=3
d['grok']=4
print(d)
for k in d:#只能从字典中提取键，不能提值
    print(k,d[k])
for k in no_d:
    print(k,no_d[k])
#%%字典推导式: dict={k:v,iteration}
#推导式都是基于一个从一个迭代器里面取元素生成了另一个数据类型的迭代器
sentence2="We need python,but c++ is more awesome"
#生成一个句子的词频的字典
counts={i:sentence2.count(i) for i in sentence2}
print(counts)
# #string。count('a')自动计算出a的次数
# print(sentence2.count('e'))

#%%运算
stock={'MT':45.23,'AAPL':31.2,'acme':51.23,'ibm':80.1}
# print(stock.values())
# print(stock.keys())
#先用zip把k-v反过来v-k
# min_price=min(zip(stock.values(),stock.keys()))
# max_price=max(zip(stock.values(),stock.keys()))
#取键
print(min(stock,key=lambda k:stock[k]))
# print(min_price)
# print(max_price)
# vk_d=zip(stock.values(),stock.keys())
# # sorted_price=(sorted(vk_d))#赋值给别的对象，可以多次访问
# print(sorted(vk_d))
# zip创建只能访问一次的迭代器,多次访问报错
# print(min(vk_d))
#%%zip sort
stock={'MT':45.23,'AAPL':31.2,'acme':51.23,'ibm':80.1}
# print(max(stock.values()))
print(max(stock,key=lambda i:stock[i]))#形参i赋值的是字典的键，返回的是值，用值作为min的key比大小,返回的是键
#若想返回值,再用键查找即可
print(stock[max(stock,key=lambda i:stock[i])])
print(sorted(stock,key=lambda i:stock[i]))#用lambda排序，或者map进行排序
# print(sorted(stock,key=lambda i:i[1],reverse=False))#X  从stock迭代器里面每次提取i为字典的key        一个（二元的）元素
#%%find相同点
da={'a':1,'b':2,'c':3}
db={'a':2,'b':2,'x':3}
print(da.keys()&db.keys())
print(da.keys()-db.keys())
print(da.items()|db.items())
#修改或者过滤字典元素:只能这样对键进行集合操作，值不可以
c={k:da[k] for k in (da.keys()-{'a','s'})}
print(c)
#键映射多值 多值映射字典
dd={'a':[1,2,3],'b':'[6,6,6]'}#列表
de={'a':{1,2,3},'b':'{6,6,6}'}#集合:元素不能重复
#%%
from collections import defaultdict
d=defaultdict(list)
d['a'].append(1)
d['a'].append(2)#同一个键插入多个值变成数列
d['b'].append(3)
print(d)
ds=defaultdict(set)
ds['a'].add(1)
ds['a'].add(2)#同一个键插入多个值变成set
ds['b'].add(3)
print(ds)
print(ds['c'])#没有key会返回一个映射到set
#%%
dd={}
dd.setdefault('a',[]).append(1)
dd.setdefault('a',[]).append(2)
dd.setdefault('a',[]).append(3)
# print(dd['b'])#没有key会报错
#所以使用defaultdict()更方便
#自定义
pairs=[('a',1),("b",2)]
#列表每个对象为两个元素的元组可以提取两个值
d={}
for key,value in pairs:
    if key not in pairs:
        d[key]=[]
    d[key].append(value)
print(d)

# ***********************dictionary end***************************************
#%%
# ********************************set*************************************
#特点{}，不允许重复;属于可变对象;无序;
#常用来去除序列的重复元素
#create
#set()是把一个迭代器对象进行实例化为结合
set1={1,2,3,4,5,6}
print(set1)
# set2={}#这样生成的是字典
# print(type(set2))
set3=set()
print(type(set3))
print(set('sdbhausfkbas'))#把striing转化成setL
#%%
set4={'xkl','asdad','gregv'}#字符串作为元素的集合
print(set4)
#dict be converted to set ,only key can be maintain
dict3={'a':1,'b':2,'c':3}
print(set(dict3))
#%%
set_num={i for i in range(10)}#推导式
set_num.add(66)
# set_num.remove(8 in set_num)#表达式结果是0或者1,不能删除8
if 8 in set_num:
    set_num.remove(8)
# set_num.remove(8)#报错
print(set_num)
#若remove元素不存在，会报错
#add()接受单个任何数据类型元素
set5={6,11,16,17}
set_num.update(set5)#加上集合，也可以加字典的key
#跟union一样，取并集
#difference取差集
#&或intersec取交集
print(set_num)










