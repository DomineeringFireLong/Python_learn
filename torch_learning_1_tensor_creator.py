import torch as t
import numpy as np
#%%
#tensor张量 是个多维数组，但其可以自动求导
#Variable是torch.autograd的数据类型，给普通的多维数组tensor加了属性，可以求grad，有参数：requires_grad需要梯度 is_leaf是否叶子节点等信息
#4.0.0版本之后，tensor直接封装了上述属性,以及：data、dtype数据类型、shape形状、device设备、requires_grad、grad、grad_fn、is_leaf等属性
#tensor本质就是加入了自动求导等很多方法的多维数组，把数据类型封装成 类，功能更多，更方便
# arr=t.tensor(np.ones((3,3)))#把基本数据类型：列表、元组 或者numpy的数据变成tensor类型 (x,y)作为shape 是一个二维的一个参数，而不是x，y两个参数
# print(arr)
# print(arr.size())#还可以访问形状


#----------------------------------tensor 创建 1.数据 2.方法 等差 均分 3.概率方法------------------------------------------

#%%
#
# arr=np.array([[1,2,3],[4,5,6]])
# t=t.from_numpy(arr)#该函数创建的张量与源数据共享内存***********************
# print(t)
# t[0,0]=6#修改数据
# t[1,2]=0#跟多维数组的索引一样
# print(arr)
#%%
#**torch.zeros()********************************依赖size的全零张量：size形状、out输出的张量、layout：内存中的布局、device、requires_grad
# t.eyes=()的区别，只有n行数也可以，或者n= m= ，默认形状是n*n的方阵，采用两个变量
# print(t.eye(3,2))#3，2 而不是(3,2)  ones() 参数是size
# out_t=t.tensor([1])
# t=t.zeros((3,3),out=out_t) #其实是一个变量，地址相同
# print(t,'\n',out_t)
# print(id(t),'\n',id(out_t))#输出；地址
#**torch.full 全为同一个值的张量******************
# arr1=t.full((3,3),6)
# print(arr1.size)
#********t.arange()等差一维张量************************
# arr2=t.arange(2,16,3)#start end step步长
# print(arr2)
#***********t.linspace()均分一维张量 start end steps(序列长度，不是步长)
# arr3=t.linspace(1,16,5)
# print(arr3.detach())#返回一个不带梯度的张量,脱离当前的张量
# print(arr3.requires_grad_(True))#修改requires_grad  返回带梯度的张量

# print(t.tensor([[1]]),t.tensor([[1]]).size())# 1*1维 tensor([[1]])
# print(t.tensor([1]),t.tensor([1]).size())#1维 tensor([1])

#*********依据 概率分布 创建 随机张量*************
#1.mean张量 std张量
# mean=t.arange(1,7,dtype=t.float32)
# std=t.arange(2,8,dtype=t.float32)
# t_nomal=t.normal(mean,std)
# print(t_nomal)#六维随机变量的正态分布
#2.mean标量 std标量
# print(t.normal(0.,1.,size=(4,))) # 4,是 一行四列 而 4，1 是四行一列
#3.一个张量，一个标量
# print(t.normal(t.arange(1,6,dtype=t.float),1))#`RuntimeError: "normal_kernel_cpu" not implemented for 'Long'` 没有dtype报错,或者 整数加.
#randn 标准正态分布  参数size
# print(t.randn((1,3)))
##t.rand()  [0,1)的均匀分布  参数size
#t.rand_like [0,1)均分分布   参数是张量
#t.randint [low,high)均分分布的整数 low= high=   size=(x,y)  大小一般都是两个数 形状才是二维元组
#t.randint_like [low,high)均分分布

# print(t.rand((2,2)))
# print(t.rand_like(t.zeros((2,3))))#生成跟输入张量形状相同的 均分分布随机张量

# t.randperm() 生成0到n-1 的随机排列，作用：随机索引
# print(t.randperm(10)) #tensor([8, 2, 6, 0, 1, 4, 5, 7, 9, 3])
# t.bernoulli() 以输入张量维概率，生成伯努利分布（0-1）
# print(t.bernoulli(t.full((3,2),0.5)))