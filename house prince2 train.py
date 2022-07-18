import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.linear_model import Ridge
from sklearn.model_selection import cross_val_score
from sklearn.ensemble import RandomForestRegressor
import warnings
warnings.filterwarnings("ignore")

train_data=pd.read_csv("/Users/bytedance/Downloads/house-prices-advanced-regression-techniques (1)/train.csv",index_col=0)
test_data=pd.read_csv("/Users/bytedance/Downloads/house-prices-advanced-regression-techniques (1)/test.csv",index_col=0)

#将两个数据连起来
data=pd.concat([train_data,test_data],ignore_index=False)

#MSSubClass是类别变量，查看其分布
#print(data["MSSubClass"].value_counts())

#避免分类数值影响，做one-hot处理
#data["MSSubClass"]=pd.get_dummies(data["MSSubClass"],prefix="MSSubClass")
data1=pd.get_dummies(data)
#print(data1.head())

#查看有空缺值的数据
null_data1=data1.isnull().sum().sort_values(ascending=False).head(10)
#print(null_data1)

#取各列数据均值填补空缺值
mean_cols=data1.mean()
data2=data1.fillna(mean_cols)
#再次查看空缺值
null_data2=data2.isnull().sum().sort_values(ascending=False).head(10)
#print(null_data2)

#数据归一化
numeric_cols=data2.columns[data2.dtypes!="object"]
numeric_cols_mean=data2.loc[:,numeric_cols].mean()
numeric_cols_std=data2.loc[:,numeric_cols].std()
data2.loc[:,numeric_cols]=(data2.loc[:,numeric_cols]-numeric_cols_mean)/numeric_cols_std

#将两个数据分开
dummy_train_data=data2.loc[train_data.index]
dummy_test_data=data2.loc[test_data.index]
#print(dummy_train_data.shape,dummy_test_data.shape)

#岭回归
#拟定不同的 50 个参数，通过交叉验证选取适合的参数
#logspace生成从10的a次方到10的b次方之间按对数等分的n个元素的行向量
alphas=np.logspace(-3,2,50)
#交叉验证，存储不同的 alpha 下，均方误差，通过绘图不同参数下的误差曲线查看最好的参 数。
x_train =dummy_train_data.values
x_test=dummy_test_data.values
y_train=np.log1p(train_data.pop("SalePrice"))
test_scores=[]

for alpha in alphas:
    clf=Ridge(alpha)
    test_score=np.sqrt(-cross_val_score(clf,x_train,y_train,cv=10,scoring="neg_mean_squared_error"))
    test_scores.append(np.mean(test_score))
#plt.plot(alphas,test_scores)
#print(plt.show())

#Random Forest 随机森林
# 随机森林主要参数: n_estimators：表示森林里树的个数； max_features：随机选择特征集合的子集合，并用来分割节点

#将树的个数作为变量，定子集 0.3 倍的特征，来探索多少树个数能得到好的效果。 同样是采用交叉验证的方式。
n_estimators = [20,50,100,150,200,250,300]
test_scores1=[]
for n in n_estimators:
    clf1=RandomForestRegressor(n_estimators=n,max_features=0.3)
    test_score1=np.sqrt(-cross_val_score(clf1,x_train,y_train,cv=5,scoring="neg_mean_squared_error"))
    test_scores1.append(np.mean(test_score1))
#作图
# plt.plot(n_estimators,test_scores1)
# print(plt.show())

#集成学习 Ensemble 选取了岭回归和随机森林两种算法，并通过类举法得到相应的好参数。 将两种”好参数“条件下的算法结果进行综合，取平均数，得到的预测值将会更准确。
ridge=Ridge(alpha=15)
rf=RandomForestRegressor(n_estimators=350,max_features=0.3)
ridge.fit(x_train,y_train)
rf.fit(x_train,y_train)
ridge.predict= ridge.predict(x_test)
rf_predict=rf.predict(x_test)
test_score2=rf.score(x_train,y_train)
print(test_score2)
y_ridge=np.expm1(rf_predict)
y_rf=np.expm1(rf_predict)

#代码中我们打印了岭回归预测准值为 0.98。虽然这个准确度是很不错，说明算法起到了预测 的效果，但提示需要注意，对训练集的预测准确度高的模型不一定就对测试集的预测效果要 好，因为可能出现”过拟合“，导致模型的泛化能力不强。 平均值 综合两个模型的预测值，取最简单的平均。
y_final=(y_rf + y_ridge)/2

#先从测试集取出 test_df.index ，并与最后预测的房价’SalePrice‘进行组合。
final_data=pd.DataFrame(data={"id":test_data.index,"SalePrice":y_final})
print(final_data)

final_data.to_csv('/Users/bytedance/Downloads/excel_output.csv')