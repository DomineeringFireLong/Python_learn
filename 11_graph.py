#方式一：用matplot绘制
import numpy as np
import matplotlib.pyplot as plt
#绘制单个图表
x=np.linspace(0,10,500)#从0到10有500个元素的等差数列
y=np.sin(x)
z=np.cos(x)
plt.plot(x,y,label="$sin(x)$",color="red",linewidth=2)#$ $中包含的会以公式表示
plt.plot(x,z,"--",label="$cos(x)$",color="blue",linewidth=2)
plt.xlabel("x")
plt.ylabel("y")
plt.ylim(-1.1,1.1)#limit限制y范围
plt.legend()#显示图例:曲线的标签和样式
plt.show()#图像显示
# plt.savefig("example1.jpg",dpi=120)#分辨率
# matplot模块中的类为包含关系，figure包含axes类，axes包含text类
# figure对象为整个窗口，而axes是其中的子图

#***绘制多个图表：subplot
# x=np.linspace(0,10,800)#从0到10有800个元素的等差数列
# y=np.sin(x)
# z=np.cos(x)
# m=np.cos(x**2)
# plt.figure("example1",figsize=(10,8),dpi=80)#创建一个figure对象：窗口example
#
#
# plt.figure("example2",figsize=(8,6),dpi=120)#创建一个figure对象：窗口example
# #都是在example2这个窗口下进行绘制
# #plot是在axes对象上绘图
# axes2_1=plt.subplot(212)#figure对象创建一个axes对象，放在下方子图
# axes2_2=plt.subplot(211)#figure对象创建一个axes对象，放在上方子图
#
# #选择子图1
# plt.sca(axes2_1)
# #设置参数
# plt.plot(x,y,label="$sin(X)$",color="red",linewidth=2)#在选择的实例对象axes子图上进行绘图
# plt.xlabel("x")
# plt.ylabel("y")
# plt.title("$sin(X)$")
# plt.ylim(-1.1,1.1)
# plt.legend()
# #选择子图2
# plt.sca(axes2_2)
# #设置参数
# plt.plot(x,z,"k-.",label="$cos(X)$",color="blue",linewidth=2)#在选择的实例对象axes子图上进行绘图
# plt.xlabel("x")
# plt.ylabel("z")
# plt.title("$cos(X)$")
# plt.ylim(-1.1,1.1)
# plt.legend()
# #在figure1窗口下绘制: #选择第一个窗口对象
# plt.figure("example1")
# plt.plot(x,m,'k-.',"m:",label="$cos(X^2)$")
# plt.xlabel("x")
# plt.ylabel("y")
# plt.title("$cos(X^2)$")
# plt.ylim(-1.1,1.1)
# plt.legend()
# #全部显示
# plt.show()

#%%****************方式二：Tkinter模块*****************
#标准GUI(Graphical User Interface)库,可以创建GUI应用程序
#canvas(画布)组件，绘制图像、图表、图像编辑器、自定义小部件：线段、多边形、圆等等
#canvas include many objects: line rectangle、text等
# if __name__ == '__main__':
#     from tkinter import *
#     root=Tk()
#     canvas=Canvas(width=900,height=650,bg="white")
#     canvas.pack(expand=YES,fill=BOTH)
#     k=1
#     j=1
#     for i in range(0,26):
#         canvas.create_oval(310-k,250-k,310+k,250+k,width=1)#左上角和右下角的坐标;从大到小画圈
#         k+=j
#         j+=0.3
#     root.mainloop()
# from tkinter import *
# root=Tk()#整个应用程序的主窗口
# # 完整的GUI应用程序，需要首先创建一个Tk实例，然后在这个实例中添加其他的控件
# canvas=Canvas(width=400,height=400,bg="white")
# canvas.pack(expand=YES,fill=BOTH)#配置曲线
# x0=263;y0=263;x1=275;y1=275
# #往左画
# for i in range(19):
#     canvas.create_line(x0,y0,x0,y1,width=1,fill='black')#实例对象的方法
#     x0-=5;y0-=5;y1+=5;x1+=5
# # 往右画
# x0=263;y0=263;y1=275
# for i in range(19):
#     canvas.create_line(x0,y0,x0,y1,width=1,fill='black')#实例对象的方法
#     x0+=5;y0-=5;y1-=5#左上角坐标是00
# root.mainloop()

#设计交互式界面

import tkinter as tk
#主窗口
top=tk.Tk()
top.title("hello test")
# 编写一个交互界面，就是要把各个组件，以适当大小，定位到界面的某个位置
#搭组件
#1.label组件
# labelhello=tk.Label(top,text="hello Tkinter")
# labelhello.pack()#组件布局管理

#2.按钮组件Button
# def btn_Clicked():
#     labelhello.config(text="hello tkinter!!!")
# labelhello=tk.Label(top,text="press here",height=5,width=20,fg="blue")
# labelhello.pack()
# btn=tk.Button(top,text='hello',command=btn_Clicked)#命令 类似于qt的槽函数
# btn.pack()#上面只是生成了组件的实例对象，pack才放入了主窗口
# top.title("botton_test")
#3.输入框组件Entry
# def btn_Clicked():
#     cd=float(entrycd.get())
#     labelhello.config(text="%.2f 的平方是 %.2f" %(cd,cd**2))
# #label
# labelhello=tk.Label(top,text="Convert x to x^2",height=5,width=20,fg="blue")
# labelhello.pack()
# #botton
# btn=tk.Button(top,text='hello',command=btn_Clicked)#命令 类似于qt的槽函数
# btn.pack()#上面只是生成了组件的实例对象，pack才放入了主窗口
# #entry
# entrycd=tk.Entry(top,text="0")
# entrycd.pack()
# top.title("Entry_test")
# top.mainloop()

#....








