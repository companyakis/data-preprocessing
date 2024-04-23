#we will use numeric data

df = data.select_dtypes(include = ["int64", "float64"])

print(df.dtypes)

"""
carat    float64
depth    float64
table    float64
price      int64
x        float64
y        float64
z        float64
"""
