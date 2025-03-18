import pandas as pd
##列表转换乘pandas数据类型
# list=[('a',25),('b',26)]
# df=pd.DataFrame(list,columns=["name","age"])#列表转化成pandas的data 有行标和列表的数组
# print(df)
#DataFrame是个二维数据，列标号为 index 行标号为 columns
df=pd.read_csv('F:/SM_3/气动数据/5/for042.csv',encoding='utf-8')
df=pd.DataFrame(df)
# print(df.shape)#不包含标号
# print(df['25'])#查询列 标号
# print(df.loc[1])#查询行 返回的是pd.series
# print(df.loc[1:3])#查询多行 这个pandas包含最后一个3
# print(df.loc[1][24])#行忽略第一行标题，列是从0开始 访问值
# print([i for i in range(1,13)])#列表生成器
# print(df.loc[[i for i in range(1,14)],'25'])#行忽略第一行标题，列是从0开始
# print(df.loc[1:13,'25']) #读取某一列的某部分
# df.loc[:,'131']=df.loc[1:13,'25']
# df.to_csv("./out.csv")
for i in range(0, 10):
    for j in range(0,13):
        df.iloc[i*13+j,2]=df.iloc[i*13+j,24]

# df.loc[1:, str(i+int('131'))] = df.loc[i * 13 + 0:i * 13 + 13, '25']
df.to_csv("./out.csv")
