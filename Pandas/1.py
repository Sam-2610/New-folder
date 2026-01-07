import pandas as pd

data = {
    'Student' : ["Amit","Sam","Sag"],
    'Rank' : [1,2,3],
    'Marks' : [20,30,34]
}

df = pd.DataFrame(data , index = ['RowA','RowB','RowC'])

print(df)

""" for cil in df:
    print(cil) """
""" print(df.loc['RowA','Student'])
print(df.loc['RowB','Rank'])
print(df.loc['RowC','Marks']) """

# print(df.iloc[[1,1]])

print(df.dtypes)
print(df.ndim)
print(df.size)
print(df.shape)
print(df.T)
print(df.index)
print(df.head(2))
print(df.tail(1))

