table_data = df.table

print(table_data.describe())

print(sns.boxplot(x = table_data))

"""
count    53940.000000
mean        57.457184
std          2.234491
min         43.000000
25%         56.000000
50%         57.000000
75%         59.000000
max         95.000000
Name: table, dtype: float64
"""

