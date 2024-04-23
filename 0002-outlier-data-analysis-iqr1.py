"""
From Khan Academy:
"
The IQR describes the middle 50% of values when ordered from lowest to highest. 
To find the interquartile range (IQR), ​first find the median (middle value) of the lower and upper half of the data. 
These values are quartile 1 (Q1) and quartile 3 (Q3). The IQR is the difference between Q3 and Q1.

"""

Q1 = df_price.quantile(0.25)

Q3 = df_price.quantile(0.75)

print("Q1 value: ", Q1)

print("Q3 value: ", Q3)

"""
Q1 value:  price    950.0
Name: 0.25, dtype: float64
Q3 value:  price    5324.25
Name: 0.75, dtype: float64
"""
