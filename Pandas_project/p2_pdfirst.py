import pandas as pd
import numpy as np
import matplotlib as plt


df =pd.read_csv('E:/python_file/PythonProject/fx_python/book2.csv')
#输出全部内容
# print(df)

#筛选一列
df['标题']
df['作者']
#切片方式筛选
#显示三行
df[1:3]

#增加列名
# df.columns = ['star','vote','shorts']

#显示特定行列
df.loc[1:3,['作者']]


#过滤数据
df['作者']=='郭菲'#显示True和False

df[df['作者']=='郭菲']#筛选出符合的那行

#缺失数据
df.dropna()#删除缺失值

#数据聚合
df.groupby('作者').sum()

#创建新列
star_to_number={
    'A':5,
    'B':4,
    'C':3,
    'D':2,
    'E':1
}
df['new_star'] = df['star'].map(star_to_number)


