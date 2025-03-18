# 张量操作：拼接、索引（切片）、变换
import torch as t
import matplotlib.pyplot as plt
# import
t.manual_seed(1)  # 设置随机种子，可以让之后的随机数 固定下来
# print(t.randn((2,2)))
# ******************************************************
# cat：把张量按维度dim进行拼接 stack在新创建的维度dim上进行拼接  两个拼接张量维度必须相同
# flag=True
flag = False
if flag:
    arr = t.ones((2, 2, 2))
    t_0 = t.cat([arr, arr], dim=0)  # 行拼接 ,0维度，就是最外面[]           torch.Size([4, 2, 2])
    t_1 = t.cat([arr, arr], dim=1)  # 列;1维度 就是第二层[]                torch.Size([2, 4, 2])
    t_2 = t.cat([arr, arr], dim=2)  # 2 维度 就是第三层[]                  torch.Size([2, 2, 4])
    # cat拼接不能再更高维度上拼，会报错
    print(t_0, '\n', t_1, '\n', t_2)
    print(t_0.shape, '\n', t_1.size(), t_2.size())

# ------------------------
# flag = True
flag = False
if flag:                           
    arr1 = t.ones((2, 3))
    arr2 = t.zeros((2, 3))
    a_s0 = t.stack([arr1, arr2], dim=0)  # 0维 插入一个维度 则 1 2维度不变   torch.Size([2, 2, 3])
    a_s1 = t.stack([arr1, arr2], dim=1)  # 1维 插入一个维度    torch.Size([2, 2, 3]) 但不一样
    a_s2 = t.stack([arr1, arr2], dim=2)  # 2维 插入一个维度    torch.Size([2, 3, 2])
    print(a_s0, '\n', a_s1, '\n', a_s2)
    print(a_s0.shape, '\n', a_s1.shape, '\n', a_s2.shape)

# flag = True
flag = False
if flag:
    a = t.ones((2, 5))
    list_of_tensors = t.chunk(a, dim=1, chunks=2)
    for idx, t in enumerate(list_of_tensors):
        print(f"第{idx}个张量{t}，shape is {t.shape}")
# split 按维度dim进行切分,可以选择每次切分的长度 split_size_or_sections 用整数 或者列表（每个部分的元素维数）
# flag = True
flag = False
if flag:
    a = t.ones((2, 5))
    list_of_tensors = t.split(a, split_size_or_sections=[2, 1, 2], dim=1)  # 列表的元素和一定与dim上元素维数相同
    for idx, t in enumerate(list_of_tensors):
        print(f"第{idx}个张量{t}，shape is {t.shape}")

# ----------------------------索引-------------------------------
# flag = True
flag = False
if flag:
    t1 = t.randint(0, 9, size=(3, 3))
    idx = t.tensor([0, 2], dtype=t.long)  # 用 列表索引
    t_select = t.index_select(t1, dim=1, index=idx)  # 0最外面的【】 是列 1里面的【】反而是行
    print(f"t:\n{t1}\nt_select:\n{t_select}")

# flag = True
flag = False
if flag:
    # masked_select(input=tensor,mask=) 按照mask中的true进行索引  mask  ge=greater or equal  gt=greater than le=less or equal lt
    t3 = t.randint(0, 9, size=(3, 3))
    mask = t3.ge(5)  # 注意mask的ge函数是张量的一个方法 返回张量
    # mask=t.tensor([[True,True,False],[False,False,False],[False,False,False]])
    # mask = t.tensor([[True, True, False]])#维数不同 默认是第0维其他默认为True  尽量维数匹配，易错
    print(t3)
    print(mask)
    print(t.masked_select(t3, mask))  # 1 0 在torch不是BoolTensor
#----------------切片-------------------
# flag = True
flag = False
if flag:
    a=t.randint(0, 9, size=(4, 3, 5, 6))
    print(a.shape) #[4, 3, 5, 6]
    print(a[:2].shape)          # [0 1] 没有2  [2, 3, 5, 6]
    print(a[:2,1].shape)        # [0 1] 1    [2, 5, 6]
    print(a[:2,-1].shape)       # [0 1] 2   [2, 5, 6]
    print(a[:2,1:,:].shape)     # [0 1] [1 2](因为是 0 1 2)    [2, 2, 5, 6]
    print(a[:2,-1:,:,:].shape)  # [0 1] [2]    [2, 1, 5, 6]
    print(a[:2,-2:,:,:].shape)  # [0 1] [1 2]    [2, 1, 5, 6]
    print(a[:,:,0:5:2,:].shape)    #[4, 3, 3, 6]     0 2 4
    print(a[:,:,::2,::2].shape) #::2 相当于 0:-1:2     [4, 3, 3, 3]
    print(a[...].shape)           #[4, 3, 5, 6]
    print(a[0,...].shape)     #[3, 5, 6]
    print(a[:,1,...].shape)  #[4, 5, 6]
    print(a[...,:2].shape)  #[4, 3, 5, 2]
# ----------------------------变换---------------------------------------------
# ------reshape(input=tenosr,shape=() )改变张量形状:两个张量共享内存
# flag = True
flag = False
if flag:
    t4 = t.randn(size=(8,))  # 1行8列
    t4_res = t.reshape(t4, (-1, 4))  # -1是其他维数固定 然后除了之后的数
    print(t4, '\n', t4_res)
    t4[0] = 6
    print(t4_res)

# -----------transpose(input=tensor,dim0,dim1) 交换的两个维度
# flag = True
flag = False
if flag:
    t4 = t.randn(size=(2, 3, 4))  # 1行8列
    t4_ = t.transpose(t4, dim0=1, dim1=2)
    print(t4, '\n', t4_)
# --------------压缩维数是1的维数suqueeze(input,dim=)------
# flag = True
flag = False
if flag:
    t1 = t.randn(size=(1, 2, 3, 1))  # 1行8列
    t1s = t.squeeze(t1)  # 2*3*1      torch.Size([2, 3])
    t1_1 = t.squeeze(t1, dim=0)  # 2*3*1      [2, 3, 1]
    t1_2 = t.squeeze(t1, dim=1)  # 1*2*3*1     [1, 2, 3, 1]
    t1_3 = t.squeeze(t1, dim=2)  # 1*2*3*1     [1, 2, 3, 1]
    # print(t1,'\n',t1_1,'\n',t1_2)
    print(t1.shape, '\n', t1s.shape, '\n', t1_1.shape, '\n', t1_2.shape, '\n', t1_3.shape)  # 只有维数是1的可以被压缩
# --------------在dim处扩展维数是1的 unsuqueeze(input,dim=)------
# flag = True
flag = False
if flag:
    t1 = t.randn(size=(1, 2, 3, 1))  # 1行8列
    # t1s = t.unsqueeze(t1)  # 必须要dim参数
    t1_1 = t.unsqueeze(t1, dim=0)  # [1, 1, 2, 3, 1]
    t1_2 = t.unsqueeze(t1, dim=1)  # [1, 1, 2, 3, 1]
    t1_3 = t.unsqueeze(t1, dim=2)  # [1, 2, 1, 3, 1]
    # print(t1,'\n',t1_1,'\n',t1_2)
    print(t1.shape, '\n', t1_1.shape, '\n', t1_2.shape, '\n', t1_3.shape)  # 只有维数是1的可以被压缩

# ---------------------------------张量数学运算--------------------------------
# 有 t. add addciv addcmul sub div mul log log10 exp pow abs cos sin atan
# flag = True
flag = False
if flag:
    t1 = t.tensor([1, 2])
    t2 = t.tensor([1, 2])
    print(t.add(t1, alpha=2, other=t2))  # t1+alpha*t2 alpha整数
    print(t.addcmul(input=t1, value=2, tensor1=t1, tensor2=t2))  # input+value*tensor1*tensor2

# -------------------------一元线性回归-----------------------------
# flag = True
flag=False
if flag:
    lr = 0.01
    # 创建数据集
    x = t.rand(20, 1) * 10
    y = 2 * x + (5 + t.randn(20, 1))
    # 构建回归模型参数
    w = t.randn((1), requires_grad=True)
    b = t.zeros((1), requires_grad=True)
    for i in range(1000):
        # 前向传播
        # y_pred=t.addcmul(input=b,value=1,tensor1=w,tensor2=x)
        wx = t.mul(w, x)
        y_pred = t.add(wx, b)
        # 计算误差
        loss = (0.5 * (y_pred - y) ** 2).mean()  # 均方差 最小二乘回归
        # 反向传播
        loss.backward()#虽然不能调用，但是实际是计算的
        # 更新参数
        b.data.sub_(lr * b.grad)#注意sub有____
        w.data.sub_(lr * w.grad)
        w.grad.zero_()
        b.grad.zero_()
        if i%20==0:
            plt.scatter(x.data.numpy(),y.data.numpy())
            plt.plot(x.data.numpy(),y_pred.data.numpy())#位置太大 不在图表范围内
            plt.text(2,20,'Loss=%.4f'%loss.data.numpy())
            plt.xlabel("x")
            plt.ylabel("y")
            plt.xlim(1.5,10)
            plt.ylim(8,28)
            plt.title(f"Iteraton:{i}\nw:{w}  b:{b}")
            # plt.legend()#显示图例:曲线的标签和样式
            # plt.show()#图像显示
            plt.pause(0.5)

            # print(f"b.grad={b.grad}")
            if loss.data.numpy()<2:
                plt.savefig("Linear_Regrassion.jpg",dpi=120)#plt.show() close都必须在save之后，否则就是白图
                break
            plt.close()