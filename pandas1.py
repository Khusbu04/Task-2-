# Display few rows
import pandas as pd 
# Create a DataFrame from a dictionary
data = {
    "Name": ["Alice", "Bob", "Charlie"],
    "Age": [25, 30, 35],
    "City": ["New York", "Los Angeles", "Chica"]
}
df = pd.DataFrame(data)
print("DataFrame:")
print(df)
# read data from a CSV file
# (Assume 'data.csv' exists in the current directory)
# df = pd.read_csv("data.csv")

# display the first few rows of the DataFrame
print("\nFirst 2 rows:")
print(df.head(2))
# Filter rows where Age > 25
filtered_df = df[df["Age"] > 25]
print("/nFiltered DataFrame:")
print(filtered_df)
# add a new column
df["Score"] = [85, 90, 88]
print("/nDataFrame with new column:")
print(df)
# save the DataFrame to a CSV file
df.to_csv("output.csv", index = False)
print("\nData saved to output.csv")