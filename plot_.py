import matplotlib.pyplot as plt
import numpy as np
import math

#图像的本质就是 利用形状、颜色、分布情况、规律、数据标注等来具体突出反映信息

plt.rcParams['font.sans-serif']=['SimHei']
plt.rcParams['axes.unicode_minus']=False

# #-------------------------------折线图(离散)----------------------------------------------

# #创建数据
# y1=[2,4,1,5,2]
# y2=[1,3,2,3,4]
# y3=[3,4,4,5,2]
# y4=[4,2,1,3,2]
# y5=[2,3,4,2,3]
# x=[i for i in range(len(y1))]
#
# #第一个窗口figure对象
# # plt.figure(num=1,figsize=(8,5))
# fig,ax=plt.subplots()
#
# line_styles=['-','--',':','-.','dashdot']
# line_colors=['b','g','r','y','purple']
# line_labels=['line 1','line 2','line 3','line 4','line 5']#图例 就是线条名称
# line_widths=[1.5,2.0,2.5,1.0,1.5]
#
# for i in range(5):
#     # trick:通过循环变量来实现对多个函数绘制不同参数图像
#     # 变量名 作为 变量 来实现循环，想实现循环画图，就得把每个图的参数写成数组形式，通过变量循环访问
#     ax.plot(x,globals()[f'y{i+1}'],linestyle=line_styles[i],color=line_colors[i],label=line_labels[i],linewidth=line_widths[i])
# # 注解工具annotate,(文本、(被注释点位置)、textcoords)textcoords被注释点的坐标系属性,xytext：注释文本的坐标点
# for i in range(len(x)):
#     ax.annotate([f'y{i+1}'],(x[i],globals()[f'y{i+1}'][i]),textcoords="offset points",xytext=(0,10),ha='center')
# #添加图例
# ax.legend()
#
# ax.set_xlabel('X轴',fontsize=12)
# ax.set_xlabel('Y轴',fontsize=12)
# #标题
# ax.set_title('折线图',fontsize=16,fontweight='bold')
# #刻度值标签字体大小
# ax.tick_params(axis='both',which='major',labelsize=10)
# #网格线
# ax.grid(True,linestyle='--',alpha=0.7)
# #背景
# ax.set_facecolor('#f0f0f0')
# #边框
# ax.spines['top'].set_color('none')
# ax.spines['right'].set_color('none')
# plt.show()
# #-------------------------------置信图(连续)----------------------------------------------
# #置信区域：就再纵坐标上下一定幅度进行填充
# plt.figure()
# x2=np.linspace(0,2,50)
# y=np.sin(x2)
# plt.plot(x2,y,color='b',label='ay')
# plt.fill_between(x2,y+0.2,y-0.2,color='lightblue',alpha=0.3,label='Confidential Interval')
# plt.show()

#----------------------------柱形图(离散):不同类别方法的同一个指标的比较------------------------------------------------------------------------
# heights=[5,6,8,4,5]
# x=[i for i in range(len(heights))]
#
# #创建窗口对象和子图对象
# fig,ax=plt.subplots()#有s
# patterns=['/','+','x','-','o']
# #patterns=['','','','','']
# colors=['blue','g','purple','r','orange']
# width=0.5
#
# for i in range(len(heights)):
#     bar=ax.bar(x[i],heights[i],width,color=colors[i],hatch=patterns[i],label=f'Bar {i+1}')
#     height=bar[0].get_height()
#     ax.annotate(f'{height}',xy=(bar[0].get_x()+bar[0].get_width()/2,height),xytext=(0,3),
#                 textcoords='offset point',ha='center',va='bottom')
# #图例
# ax.legend(fontsize=12,loc='upper right')
#
# ax.set_xlabel('X轴',fontsize=12)
# ax.set_xlabel('Y轴',fontsize=12)
# plt.ylim([0,10])
# #标题
# ax.set_title('条形图',fontsize=16,fontweight='bold')
# #刻度值标签字体大小
# ax.tick_params(axis='both',which='major',labelsize=10)
# #网格线
# ax.grid(axis='y',linestyle='--',alpha=0.7)
# #背景
# ax.set_facecolor('#f0f0f0')
# #去除边框
# for spine in ax.spines.values():
#     spine.set_visible(False)
# plt.show()

#----------------------------直方图(离散):同类别方法的同一个指标的值 多次测试统计其频数------------------------------------------
# colors=['blue','g','purple','r','orange']
# np.random.seed(0)
# data1=np.random.normal(0,1,100)#正态分布
# fig,ax=plt.subplots()
# bins=20
# color=['g']
# #直方图:只输入一个y变量
# ax.hist(data1,bins=bins,color=colors[0],hatch='/',alpha=0.7,label='Group',edgecolor='black')
# ax.legend()
# ax.set_xlabel('数值',fontsize=12)
# ax.set_xlabel('频次',fontsize=12)
# ax.set_title('直方图',fontsize=14)
# ax.tick_params(axis='both',which='major',labelsize=10)
# ax.set_facecolor('#f0f0f0')
# ax.spines['top'].set_color('none')
# ax.spines['right'].set_color('none')
# plt.show()

#----------------------------散点图(离散):同类别方法的同一个指标的值 多次测试统计其频数------------------------------------------------------------------------
# 1.聚类
# from sklearn.cluster import KMeans
# np.random.seed(0)
# data=np.random.rand(100,2)*5 #[0,5) 100个数
# num_clusters=3
# km=KMeans(n_clusters=num_clusters,random_state=0)#不是k_means 不同的api参数不同 用法不同
# labels=km.fit_predict(data)#聚类结果
# fig,ax=plt.subplots()
# colors=['tab:blue','tab:orange','tab:purple']
# markers=['o','s','D']#形状
# for i in range(num_clusters):
#     cluster_data=data[labels==i]
#     ax.scatter(cluster_data[:,0],cluster_data[:,1],marker=markers[i],color=colors[i],label=f'Cluster{i+1}')
# ax.legend()
# plt.tight_layout()
# plt.show()
#2.单纯散点图
# x=np.random.rand(50)
# y1=np.random.rand(50)
# y2=np.random.rand(50)
# y3=np.random.rand(50)
# y4=np.random.rand(50)
# y5=np.random.rand(50)
# fig,ax=plt.subplots()
# ax.scatter(x,y1,marker='o',color='b',label='Group 1')
# ax.scatter(x,y2,marker='x',color='g',label='Group 2')
# ax.scatter(x,y3,marker='+',color='r',label='Group 3')
# ax.scatter(x,y4,marker='*',color='c',label='Group 4')
# ax.scatter(x,y5,marker='s',color='m',label='Group 5')
# ax.legend()
# plt.show()

#----------------------------饼状图(离散):比例、对比-----------------------------------------------------------------------

# labels1=['Group 1','Group 2','Group 3']
# labels2=['Group 4','Group 5','Group 6']
# size1=[30,20,50]
# size2=[25,35,30]
# colors1=['tab:blue','tab:orange','tab:purple']
# colors2=['tab:red','tab:green','tab:brown']
#
# fig,ax=plt.subplots()
# #双层饼图,注意超参数拼写
# wedges1,texts1,autotext1=ax.pie(size1,pctdistance=0.8,labels=labels1,colors=colors1,autopct="%1.2f%%",
#                                 startangle=90,wedgeprops=dict(edgecolor='w'))#1.1一位小数 1.2两位, startangle从多少度开始画,边框颜色,字体位置半径
# wedges2,texts2,autotext2=ax.pie(size2,pctdistance=0.6,labels=labels2,radius=0.5,colors=colors2,autopct="%1.2f%%",
#                                 startangle=90,wedgeprops=dict(edgecolor='w'))
#
# for autotext in autotext1+autotext2:
#     autotext.set_fontsize(15)
# ax.legend(wedges1+wedges2,labels1+labels2,loc='best')
# ax.set_title("饼图",fontsize=14,fontweight='bold')
#
# plt.show()
#----------------------------箱线图(离散):展示多个统计特征-----------------------------------------------------------------------
## shift+ait 竖选
# np.random.seed(0)
# data1=np.random.normal(0,1,100)
# data2=np.random.normal(2,1.5,100)
# data3=np.random.normal(-2,1.5,100)
# data4=np.random.normal(3,1,100)
# data5=np.random.normal(-1,0.5,100)
# fig,ax=plt.subplots()
#
# boxes=ax.boxplot([data1,data2,data3,data4,data5],labels=['group 1','group 2','group 3','group 4','group 5'],sym='o',vert=True,patch_artist=True)
# colors=['tab:blue','tab:orange','tab:purple','tab:red','tab:green']
# #设置颜色
# for box,color in zip(boxes['boxes'],colors):
#     box.set(facecolor=color)
#
# ax.legend(boxes['boxes'],['group 1','group 2','group 3','group 4','group 5'],loc='upper right')
#
# plt.show()

#----------------------------热力(连续):用颜色突出信息的程度区别 -------------------------------------------------------------
# data=np.random.randint(1,10,size=(10,10))
# fig,ax=plt.subplots()
# heatmap=ax.imshow(data,cmap='hot', interpolation="nearest", aspect="auto")#cmap=颜色渐变参数
# #颜色条
# cbar=plt.colorbar(heatmap,fraction=0.046,pad=0.04)
# plt.show()

##----------------------------等高线图(连续) -------------------------------------------------------------
# x=np.linspace(-10,10,100)
# y=np.linspace(-10,10,100)
# X,Y=np.meshgrid(x,y)
# Z=X**2-Y**2
# fig,ax=plt.subplots()
# #等高线图
# coutour=ax.contour(X,Y,Z,levels=30,cmap='coolwarm',linewidths=1)
#
# cbar=plt.colorbar(coutour,ax=ax)
#
# plt.show()


#---------------------------------------气泡图(连续):用大小和位置来反应信息 -------------------------------------------------------------
# x=np.random.rand(50)
# y=np.random.rand(50)
# size=np.random.randint(100,500,50)#50个气泡
# color=np.random.rand(50)
# fig,ax=plt.subplots()
# #气泡图其实就是散点图放大
# scatter=ax.scatter(x,y,s=size,c=color,cmap='coolwarm',alpha=0.7,edgecolors='k')
# cbar=plt.colorbar(scatter)
# plt.show()

#-----------------------------------------雷达图：反应一个事物的多方面属性-------------------------------------------------------------
# categories=['A','B','C','D','E']#五种属性
# value1=[4,2,3,5,6]
# value2=[2,5,1,2,4]
# value3=[3,4,6,3,5]
# #将第一维数据复制到最后，形成闭合
# value1+=value1[:1]
# value2+=value2[:1]
# value3+=value3[:1]
# #计算每个维度的角度
# angles=np.linspace(0,2*np.pi,len(categories),endpoint=False)
# #角度和数值对应
# angles=np.concatenate((angles,[angles[0]]))
# #使用 极坐标系来绘制的折线图
# fig,ax=plt.subplots(subplot_kw={'projection':'polar'})
#
# ax.plot(angles,value1,linewidth=1.5,linestyle='--',color='b',label="data1")
# ax.fill(angles,value1,alpha=0.3,color='b')
# ax.plot(angles,value2,linewidth=1.5,linestyle='-.',color='g',label="data2")
# ax.fill(angles,value2,alpha=0.3,color='g')
# ax.plot(angles,value3,linewidth=1.5,linestyle='--',color='r',label="data3")
# ax.fill(angles,value3,alpha=0.3,color='r')
#
# ax.legend(loc="upper right",fontsize=12)
# plt.show()

#-----------------------------------------网络图(链接图)： -------------------------------------------------------------
# import networkx as nx
# G=nx.Graph()
# G.add_nodes_from([i+1 for i in range(6)])
# G.add_edges_from([(1,2),(2,3),(3,4),(4,5),(5,1),(1,3),(4,6)])
# pos=nx.circular_layout(G)#设置节点位置
# nx.draw_networkx_nodes(G,pos,node_color='skyblue',node_size=1000,label='节点')
# nx.draw_networkx_edges(G,pos,edge_color='gray',width=2)
# nx.draw_networkx_labels(G,pos,font_size=12,font_weight='bold')
# plt.show()

#-----------------------------------------桑基图(数据传输图)： -------------------------------------------------------------
#需要其他库


#----------------------------------------------三维函数图-----------------------------------------------------------------

x=np.linspace(-5,5,100)
y=np.linspace(-5,5,100)
X,Y=np.meshgrid(x,y)
Z=np.sin(np.sqrt(X**2+Y**2))
#3D对象
fig=plt.figure(figsize=(10,6))
ax=fig.add_subplot(111,projection='3d')
surf=ax.plot_surface(X,Y,Z,cmap='viridis',edgecolor='black',alpha=0.8)
#设置刻度标签
ax.set_xticks(np.arange(-5,6,2))
ax.set_yticks(np.arange(-5,6,2))
ax.set_zticks(np.arange(-1,1.5,0.5))
#轴范围
ax.set_xlim(-5,5)
ax.set_ylim(-5,5)
ax.set_zlim(-1,1)
#添加颜色条
fig.colorbar(surf,shrink=0.5,aspect=5)
#初始视角
ax.view_init(elev=30,azim=30)
#隐藏边框
ax.xaxis.pane.fill=False
ax.yaxis.pane.fill=False
ax.zaxis.pane.fill=False
ax.xaxis.pane.set_edgecolor('w')
ax.yaxis.pane.set_edgecolor('w')
ax.zaxis.pane.set_edgecolor('w')
ax.grid(True)
plt.show()

#----------------------------------------------三维散点图-----------------------------------------------------------------

# np.random.seed(0)
# cluster1=np.random.randn(100,3)+[3,3,3]#100个 三维 基准点周围
# cluster2=np.random.randn(100,3)+[-2,-2,-2]#100个 三维 基准点周围
# cluster3=np.random.randn(100,3)+[1,-1,4]#100个 三维 基准点周围
#
# #窗口对象
# fig=plt.figure(figsize=(10,8),frameon=False)
# #图像对象
# ax=fig.add_subplot(111,projection='3d')
# #图像上加入数据点
# ax.scatter(cluster1[:,0],cluster1[:,1],cluster1[:,2],color='r',marker='o',label='Cluster 1',alpha=0.6)
# ax.scatter(cluster2[:,0],cluster2[:,1],cluster2[:,2],color='g',marker='^',label='Cluster 2',alpha=0.6)
# ax.scatter(cluster3[:,0],cluster3[:,1],cluster3[:,2],color='b',marker='s',label='Cluster 3',alpha=0.6)
# ax.legend(loc='upper right')
#
# ax.set_xlabel('X')
# ax.set_ylabel('Y')
# ax.set_zlabel('Z')
# plt.title("三维散点图",fontsize=16,fontweight='bold')
# #坐标轴范围
# ax.set_xlim(-6,6)
# ax.set_ylim(-6,6)
# ax.set_zlim(-6,6)
# #坐标轴刻度
# ax.set_xticks(np.arange(-6,7,2))
# ax.set_yticks(np.arange(-6,7,2))
# ax.set_zticks(np.arange(-6,7,1))
# # #隐藏边框
# ax.xaxis.pane.fill=False
# ax.yaxis.pane.fill=False
# ax.zaxis.pane.fill=False
# ax.xaxis.pane.set_edgecolor('w')
# ax.yaxis.pane.set_edgecolor('w')
# ax.zaxis.pane.set_edgecolor('w')
# plt.show()

#----------------------------------------------三维柱状图-----------------------------------------------------------------
# x=[1,2,3]
# y=[1,2,3,4,5]
# z=[[5,4,2],
#    [7,6,3],
#    [7, 5, 4],
#    [6, 7, 3],
#    [5, 6, 2]]
# fig=plt.figure(figsize=(10,8))
# ax=fig.add_subplot(111,projection='3d')
#
#
# dx=dy=0.3#柱子的宽度
# dz=[row[0] for row in z]
# color=['tab:red','y','tab:green']
# #绘制图像
# for i in range(len(x)):
#     for j in range(len(y)):
#         ax.bar3d(x[i],y[j],0,dx,dy,dz[j],shade=True,color=color[i],edgecolor='black',linewidth=1,alpha=0.6)
# #虚拟图例
# # 图
# rect1=plt.Rectangle((0,0),1,1,fc=color[0],edgecolor='black',linewidth=1)
# rect2=plt.Rectangle((0,0),1,1,fc=color[1],edgecolor='black',linewidth=1)
# rect3=plt.Rectangle((0,0),1,1,fc=color[2],edgecolor='black',linewidth=1)
# # 例
# ax.legend([rect1,rect2,rect3],['Category 1','Category 2','Category 3'],loc='upper left')
# ax.set_xlabel('X轴')
# ax.set_xlabel('Y轴')
# ax.set_xlabel('Z轴')
# plt.show()


