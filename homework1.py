# Action1:求2+4+...100的结果
sum = 0
for v in range(2, 101, 2):
    sum += v
print('2+4+6+...+100=', sum)

# Action2:统计全班成绩
import pandas as pd

data = {
    "姓名": ["张飞", "关羽", "刘备", "典韦", "许褚"],
    "语文": [68, 95, 98, 90, 80],
    "数学": [65, 76, 86, 88, 90],
    "英语": [30, 98, 88, 77, 90],
}
df = pd.DataFrame(data)
subjects = df.columns[1:]
for column in subjects:
    print(column, "课成绩平均值，最大值，最小值，方差，标准差依次为：", df[column].mean(), df[column].max(), df[column].min(), df[column].var(),
          df[column].std())

df['总分'] = df[subjects].sum(axis=1)
df = df.sort_values('总分')
print(df)

# Action3：对汽车质量数据进行统计
# 数据加载
df = pd.read_csv('./car_data_analyze/car_complain.csv')
# 按逗号分割problem列
df = df.drop('problem', axis=1).join(df.problem.str.get_dummies(','))


# 数据清洗,将别名合并
def f(x):
    x = x.replace('一汽-大众', '一汽大众')
    return x


df['brand'] = df['brand'].apply(f)

# 按brand统计投诉总数
df1 = df.groupby(['brand'])['id'].agg(['count'])
print(df1)

# 按car_model统计投诉总数
df2 = df.groupby(['brand', 'car_model'])['id'].agg(['count'])
print(df2)

# 重新构造新的dataframe，columns为品牌、车型、投诉数
df2.reset_index(inplace=True)

# 统计每个品牌平均每个车型的投诉数
df3 = df2.groupby(['brand'])['count'].agg(['mean'])
# 从大到小排序
df3 = df3.sort_values('mean', ascending=False)
print('平均车型投诉数最多的品牌是:',df3.index[0],'\n','平均投诉数为：',df3['mean'][0])
