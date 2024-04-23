#null values is important, but now we don't want to consider them

print(df.isnull().sum())

#As we see, there is no null value!

"""
carat    0
depth    0
table    0
price    0
x        0
y        0
z        0
dtype: int64
"""
