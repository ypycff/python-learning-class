import pandas as pd

# Read a csv file, get a DataFrame back.
df = pd.read_csv('WorldCupWinners1.txt', names=['Teams','Wins'])

# DataFrame has a describe() method, which give a summary about the data.
print("\nData description:\n%s" % df.describe())

# We can also display all the DataFrame data if we like.
print("\nAll the data:\n%s" % df)

# Sort the data, on the 'Wins' column.
sortedDf = df.sort_values(['Wins'], ascending=False)
print("\nSorted teams\n%s" % sortedDf)
