import pandas as pd
# print(pd.__version__)
df = pd.read_csv("https://raw.githubusercontent.com/datasciencedojo/datasets/master/titanic.csv")
#print(df.head(10))
df.set_index('PassengerId',inplace=True)
# print(df.loc[[1,2,3]])
# print(df.loc[[1,2],['Name', 'Sex','Age']])
# print(df.loc[10:20])
# print(df.loc[10:30:2])
# print(df.loc[1:10,['Name', 'Sex','Age']])
# print(df.query('Age > 20').head())
# print(df.query('Age > 20 & Sex=="male"').head())
#df.to_csv('dataset.csv',sep=';',index=False,encoding='utf-8-sig')


print(df.query('Age < 18').head())
df.to_csv('crianca.csv',sep=';',index=False,encoding='utf-8-sig')
