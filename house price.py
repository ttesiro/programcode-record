import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import warnings
warnings.filterwarnings("ignore")

data=pd.read_csv("/Users/bytedance/Downloads/house-prices-advanced-regression-techniques (1)/train.csv")


#相关性矩阵
k=10
corr=data.corr()
print("corr结果\n",data)
cols=corr.nlargest(k,"SalePrice")["SalePrice"].index   #取前10个相关性最高的，并且列出index的值，也就是列标题
print("cols结果\n",cols)
cn=np.corrcoef(data[cols].values.T)
sns.set(font_scale=1.25)
heatmap=sns.heatmap(cn,cbar=True,linewidths=1,vmax=1.0, square=True,linecolor='white', annot=True,
                    yticklabels=cols.values,xticklabels=cols.values)
print(plt.show())

