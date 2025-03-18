import torch as t
#计算图的理解，链式求导
# w=t.tensor([1.],requires_grad=True)
# x=t.tensor([2.],requires_grad=True)
#
# a=t.add(w,x)
# a.retain_grad()#保留中间节点的梯度
# b=t.add(w,1)
# y=t.mul(a,b)
#
# y.backward()
# print("is_leaf:\n",w.is_leaf,x.is_leaf,a.is_leaf,b.is_leaf,y.is_leaf)
# print("gradient",w.grad,x.grad,a.grad,b.grad,y.grad)#非叶子节点的梯度反向传播后会释放
# print("gradient_function",w.grad_fn,x.grad_fn,a.grad_fn,b.grad_fn,y.grad_fn)# 叶子节点没有梯度函数


#pytorch采用的是动态图机制，tensflow采用静态图；
# 前者 运算和搭建同时进行，灵活 易调节；后者 先搭建图 后运算 不灵活但效率高



#--------autograd 自动求导------------- autograd.grad
#要想求高阶导数：如二阶导数，需要给导数设置 create_grapg=True 来保留梯度
# flag=True
flag=False
if flag:
    w=t.tensor([1.],requires_grad=True)
    x=t.tensor([2.],requires_grad=True)

    a=t.add(w,x)
    a.retain_grad()#保留中间节点的梯度
    b=t.add(w,1)
    b.retain_grad()
    y0=t.mul(a,b)
    y1=t.add(a,b)
    #多变量的损失函数
    loss=t.cat([y0,y1],dim=0)# [(w+x)*(w+1),((w+x)+(w+1))]
    # print(loss)#[6., 5.] 向量
    grad_t=t.tensor([1.,1.])#梯度权重 (w+x)*(w+1)+3((w+x)+(w+1))
    loss.backward(gradient=grad_t,retain_graph=True)#按权重求和计算梯度
    print(w.grad)#(w+1)+(w+x) + 6 =2+3 6  [11.]
    # w.grad.zero_()#梯度清零后 再求还是一阶导
    grad_t2=t.tensor([1.,1.])#不是二阶导
    loss.backward(gradient=grad_t2)#向量不能求梯度，必须有该参数内积变成标量，否则报错RuntimeError: grad can be implicitly created only for scalar outputs
    print(w.grad)#  这种向量求不是二阶偏导数
# flag=True
flag=False
if flag:
    x=t.tensor([1.],requires_grad=True)#. 变成浮点数 Only Tensors of floating point and complex dtype can require gradients
    y=t.mul(x,x)#尽量用torch运算
    y=t.mul(y,x)
    y.backward(retain_graph=True)
    print(x.grad)#3*x^2
    x.grad.zero_()#_表示就地操作，梯度清零 就不进行累计求高阶导数
    y.backward()
    print(x.grad)#6*x  二阶导数



# flag=True
flag=False
if flag:
    w=t.tensor([1.],requires_grad=True)
    x=t.tensor([2.],requires_grad=True)

    a=t.add(w,x)
    b=t.add(w,1)
    y0=t.mul(a,b)
    y1=t.add(a,b)
    loss=t.add(y0,y1)#(w+x)*(w+1)+((w+x)+(w+1))
    #二阶偏导数
    grad_1=t.autograd.grad(outputs=loss,inputs=w,create_graph=True)
    print(grad_1)#[7.]  (w+x)+(w+1)+2  7 对x一阶导 (w+1)+1 3
    grad_2 = t.autograd.grad(outputs=grad_1, inputs=w)
    print(grad_2)#[2.]   2        [[2 1],[1 0]]
    #并非二阶偏导数：而是两次求导的乘积
    # loss.backward(retain_graph=True)
    # print(w.grad)#7
    # loss.backward()
    # print(w.grad)#14


#autograd注意：1.梯度不会自动清零，反向传播后记得清零，要不就是高阶导数的累乘
#2.依赖于叶子结点的结点，requires_grad默认True
#3。叶子节点不能执行 in-place操作:在原始内存中改变数据

# flag=True
flag=False
if flag:
    a=t.ones((1,))
    print(id(a),a)
    # a=a+t.ones((1,))#该操作改变了地址，不是就地操作
    a.add_(1)#就地操作
    print(id(a),a)


#Logistic Regression 逻辑回归：线性的二分类问题
#sigmoid 1/(1+e^(-x))
#线性回归是拟合y与x关系 y=wx+b 连续，而逻辑回归 y=1/((1+e^(-wx+b)))

#机器学习=数据+模型+损失函数+优化器+训练（反复迭代更新）
import torch.nn as nn
import matplotlib.pyplot as plt
import numpy as np
#数据
t.manual_seed(1)
sample_nums=100
mean_value=1.7
bias=1
n_data =t.ones(sample_nums,2)
#类别0
x0=t.normal(mean_value*n_data,1)+bias# 100,2
y0=t.zeros(sample_nums)#100,1
#类别1
x1=x0=t.normal(-mean_value*n_data,1)+bias# 100,2
y1=t.ones(sample_nums)# 100,1
train_x=t.cat((x0,x1),0)
train_y=t.cat((y0,y1),0)
#模型
class LR(nn.Module):
    def __init__(self):
        super(LR, self).__init__()
        self.f1=nn.Linear(2,1)
        self.sigmoid= nn.Sigmoid()

    def forward(self,x):
        x=self.f1(x)
        x=self.sigmoid(x)
        return x

mynet=LR()
loss_fn=nn.BCELoss()
lr=0.01
optimizer=t.optim.SGD(mynet.parameters(),lr=lr,momentum=0.9)

for i in range(500):
    y_pred=mynet(train_x)#自动进行批量化
    loss=loss_fn(y_pred.squeeze(),train_y)
    loss.backward()
    optimizer.step()
    if i%20==0:
        mask=y_pred.ge(0.5).float()#0.5为阈值分类,预测值在0.5以上就是1 否则是0 进行二值化
        # print(mask)
        correct = (mask==train_y).sum()#正确样本个数
        print(correct)
        acc=correct/200#率
        plt.figure()
        plt.scatter(x0.data.numpy()[:,0],x0.data.numpy()[:,1],c='r',label="class1")
        plt.scatter(x1.data.numpy()[:, 0], x1.data.numpy()[:, 1], c='b',label="class2")
        w0,w1=mynet.f1.weight[0]
        w0, w1 =float(w0.item()),float(w1.item())
        plot_b=float(mynet.f1.bias[0].item())
        plot_x=np.arange(-6,6,0.1)
        plot_y=(-w0*plot_x-plot_b)/w1

        plt.xlim(-5,7)
        plt.ylim(-7,7)
        plt.plot(plot_x,plot_y)
        plt.text(-5,5,'loss=%4.f' %loss.data.numpy())
        plt.title("Iteration:{}\n accuracy:{:.2%}".format(i,acc))
        plt.legend()
        plt.show()
        plt.pause(0.5)
        plt.close()
        if acc>0.95:
            break