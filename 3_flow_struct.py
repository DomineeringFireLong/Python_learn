import numpy as np
import pandas as pd
#python没有switch case
#for i in object
#从object取出来数据给i，内存并不公用，实际上相当于调用函数的形参和实参关系，改变实参，不改变实参
#enumerate 枚举 实现遍历元素 从默认0开始
list1=['a','b','c','d']
for index,data in enumerate(list1,start=1):
    data="xiaokonglong"
    print('{} is {}'.format(index,data))
print(list1)

#%%
# #break 跳出离他最近的该整个循环，continue跳出离他最近的本轮次的循环
# for x in range(6):
#     if x>5:
#         break
#     print(x,end='\t')
#     x+=1
for x in range(6):
    if x==2:
        continue
    print(x,end='\t')
    x+=1
#%%
# pass 无实用但需要语句时 填充函数体
#定义函数时 先用pass填充，待之后编程时再代替
#%% fibonacci
f=[]
f.append(0);f.append(1)
print(f)
for j in range(10):#从0-9
    i=j+2
    f.append(f[i-1]+f[i-2])
    print('f{}= {}'.format(i,f[i]))
print(f)
#%% 算法本质是从数学原理计算的算法延申出的广义概念
#双分支 if else 多分枝 if elif elif else:
#for-else语句
hobbies=""
for i in range(1,3+1):
    s=input('请输入爱好之一(按q结束)=')
    if s.upper()=='Q':#把字符串改为大写upper   ower小写
        break#跳出整个for循环 不执行下面的else
    hobbies+=s+" "
else:#for循环最后执行一次，如果提取break则不执行
    print("您输入了三个爱好")
print('您的爱好是:',hobbies)
#%%zip函数：多个可迭代的对象按顺序标号对应元素打包成一个元组，然后返回列表对象（元组为其元素），返回长度取最短
#*zip解压出变量
x=[1,2,3]
y=[4,5,6]
# print(zip(x,y))#地址
print((x,y))#列表串联组成元组
print(*zip(x,y))#元组
#*zip()函数是zip()函数的逆过程，将zip对象变成原先组合前的数据
a,b=zip(*zip(x,y))
print(a,b)#解压提取出x,y
print(list(zip(x,y)))#以元组为元素的列表
#zip实现两个迭代对象的并行循环
for i,j in zip(x,y):
    print("{}*{}={}".format(i,j,i*j))
#%%
#******map循环****************
# map(func, *iterables) 把func作用于整个迭代对象的每个元素，映射
# list[]
list(map(abs,[-1,2,5,-1,8,6]))
list(map(pow,range(1,5),range(0,4)))#次幂
list(map(lambda x,y:x+y,'abc','de'))#自定义，字符串拼接



