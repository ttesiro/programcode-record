#加载情感分析模块
from snownlp import SnowNLP
from snownlp import sentiment
import pandas as pd
import matplotlib.pyplot as plt
#导入样例数据
aa ='/Users/bytedance/Downloads/评论.xlsx'
#读取文本数据
df=pd.read_excel(aa)
print(df.head())

df['评论内容'] = df['评论内容'].apply(str)
#评论内容提取所有数据
df1=df.iloc[:,6]
print('将提取的数据打印出来：\n',df1)


#遍历每条评论进行预测
values=[SnowNLP(i).sentiments for i in df1]
#输出积极的概率，大于0.5积极的，小于0.5消极的
#myval保存预测值
myval=[]
good=0
bad=0
for i in values:
   if (i>=0.5):
       myval.append("正面")
       good=good+1
   else:
       myval.append("负面")
       bad=bad+1
df['预测值']=values
df['评价类别']=myval
#将结果输出到Excel
df.to_excel('/Users/bytedance/Downloads/评论.xlsx')
rate=good/(good+bad)
print('好评率','%.f%%' % (rate * 100)) #格式化为百分比
#作图
y=values
plt.rc('font', family='SimHei', size=10)
plt.plot(y, marker='o', mec='r', mfc='w',label=u'评价分值')
plt.xlabel('用户')
plt.ylabel('评价分值')
# 让图例生效
plt.legend()
#添加标题
plt.title('京东评论情感分析',family='SimHei',size=14,color='blue')
plt.show()

