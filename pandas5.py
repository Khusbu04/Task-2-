#sorting and Ranking
import panda as pd 
data = {
    "Name": ["Alice", "Bob", "Charlie", "David"],
    "Score": [85, 92, 88, 75]
}
df = pd.DataFrame(data)
# Sort by score in descending order
sorted_df = df.sort_values(by = "Score", ascending = False)
print("DataFrame sorted by Score:")
print(sorted_df)
# Add a rank column
df["Rank"] = df["Score"].rank(ascending = False)
print("\nDataframe with Rank:")
print(df)