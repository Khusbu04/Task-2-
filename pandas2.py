# Finding the missing data
import pandas as pd 
import numpy as np 
data = {
    "Name": ["Alice", "Bob", "Charlie", "David"],
    "Age": [25, np.nan, 35, 40],
    "City": ["New York", "Los Angeles", "Chicago", None]
    }
df = pd.DataFrame(data)
print("Original DataFrame:")
print(df)
# Fill missing values
df["Age"].fillna(df["Age"].mean(), inplace = True)
df["City"].fillna("Unknown", inplace = True)
print("\nDataFramw after filling missing values:")
print(df)
# Drop rows with missing values
df = df.dropna()
print("\nDataFrame after dropping rows with missing values:")
print(df)