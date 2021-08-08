import pandas as pd 

# All the World Cup winners, including the probable winners in 2022, i.e. Wales :-)
teams = ['Brazil','England','France','Italy','Spain','Uruguay','West Germany', 'Germany', 'Argentina', 'Wales'];

# How many times each country has won the cup (e.g. Brazil have won the World Cup 5 times).
wins  = [5, 1, 2, 4, 1, 2, 3, 1, 2, 1];

# Create a list of tuples. Each tuple is a (team, wins) pair.
stats = list(zip(teams,wins));
print(stats);

# Create a Pandas DataFrame. This is the main data type in Pandas.
# See http://pandas.pydata.org/pandas-docs/stable/generated/pandas.DataFrame.html
df = pd.DataFrame(data = stats, columns=['Teams', 'Wins']);
df.index.name = 'Index';
df.to_csv('WorldCupWinners1.txt',index=False,header=False);
df.to_csv('WorldCupWinners2.txt',index=True,header=True);

