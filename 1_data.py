import sys
import pprint
import numpy


x=2,5
print(x)
print(x==(2,5))


#%%
#format格式化
print('{} is {}'.format('james','king'))
print('{0} is {1},but "{0}!"'.format('james','awesome','handsome'))
print('{name} is {para1},but {para2}'.format(name='james',para1='awesome',para2='handsome'))
table={'Baidu':1,'Ali':2,'Tencent':3}
print(type(table))
for name,number in table.items():
    print('{:10} ==> {:10}'.format(name,number)) # ：+数字  设置该域最小宽度

#%%
#**********书写规范*************
#不能有空格缩进
#\反斜杠 一行代码太多 续行符
#;一行可以写多条语句
#符合语句if for while def class等,其构造体语句为下行的缩进代码(4个空格)，对齐就行

for i in range(1,11):
    print(i,end='  ')
#**********书写规范*************

#%%
#****************运算符:***********************
#算数 **幂运算 //整除 /除 %取余  有重载 对不同数据类型的作用不同  str+str串联  str*3 重复三次
#赋值运算 支持 a *=a *可以为算数运算符 但是不支持++ --
#关系 ==等于 !=不等
#逻辑 and or not
#位操作 &按位与 |按位或 ~按位非 按位异或^ 左移<<  右移>>
#成员测试运算符 in not in

# a_list=['a','b','c','d'];a='a';print(a in a_list);print('e' not in a_list)

#身份（同一性测试）运算符 is is not
#a is b a与b指向同一个对象(地址相同)为真
#id()标识符 查看地址
#
list1=['a','b','c','d']
print(id(list1))
list2=list1#拷贝赋值 是共享同一个地址
print(id(list2))
print(list1 is list2)
# list3=['a','b','c','d']
list3=list1[:]#这种赋值不是拷贝，地址不同
print(list3)
print(id(list3))
print(list3 is list1)


#****************运算符:***********************

#%%






#%%

# x = sys.stdin.read(6)#读入先6个字符
# x=sys.stdin.readline()#一直读入数据直到回车
# x=sys.stdin.readline(5)#读入数据只取前5字符

# print(x)


# a=['a','b','c']
# b='dabazi'
# c=[[1,2,3],[4,5,6],[1],[2,3,4,5,4]]#2维列表
# d=[[[1,2,3],[1],[22]],[1],[2]]#3维列表,从0开始索引
# e=((1,2,3),(2,1),(3,2,1,0))#2维元组
# f=((1,(1,2,3),3),(2,(1,2),1),(3,(2),1,0))#3维元组
# del a
# print(a)#列表和字符串不能用一个print输出
# print('\n'+b)#列表和字符串不能用一个print输出
# print(c)
# print(c[3][0])
# print(d)
# print(d[0][0])
# d[0][0][2] = 10#列表中数据可以改
# print(d[0][0])
#list 本质就是 数组的数据结构
# print(e)
# e[0][1]=10
# print(e)
# print(f[0][1][1])
# e[0][0][2] = 10#列表中数据可以改
# print(e[0][0])
#tuple 数组的数据结构

# print(2**3) #** 为^
# print(1e-4)# 10^
# print(bool(0))#只有0为false 负数也是true
# x=eval(input("Input a number: \n"))#eval提取输入数据的类型
# print(type(x))
#不同类型的数据不能放在一个print
# print("number:"+x+"type")
# print(type(x))
# data=("list",[1,2,3,4,5,6],
# #       'another list',[1,0,2,3,4])
# data=["list",[1,2,3,4,5,6],
#       'another list',[1,0,2,3,4]]#列表和元组都可以存储不同的数据类型
# print(type(data))
# # print(data)
# pprint.pprint(data,width=50)
#%%
