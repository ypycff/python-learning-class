import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# Read a csv file, get a DataFrame back.
df = pd.read_csv('WorldCupWinners1.txt', names=['Teams','Wins'])

# Call the plot() function, to "remember to plot a barchart".
df.plot(kind='bar', color=[["violet", "pink", "blue", "yellow"]])

# Set the labels on the barchart.
plt.xlabel('Teams')
plt.ylabel('Wins')

# Set the ticks on the x axis.
teams = df.Teams.values
plt.xticks(np.arange(len(teams)), teams, rotation=45)

# Set the position of the figure within the drawing window.
plt.subplots_adjust(left=0.1, right=0.9, top=0.9, bottom=0.25)

# Display the figure. Only now does it actually get displayed.
plt.show() 
