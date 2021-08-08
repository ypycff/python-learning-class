''' 
matplotlib.pyplot is a collection of functions that make matplotlib work like MATLAB. 
Each pyplot function makes some change to a figure: e.g., 
 - create a figure
 - create a plotting area in a figure
 - plot some lines in a plotting area
 - decorate the plot with labels
 - etc. 
Various info is remembered across function calls, e.g. the current figure and plotting area. 
For a nice tutorial, see http://matplotlib.org/users/pyplot_tutorial.html
'''

# Import the matplotlib.pyplot module, which contains the plotting functions etc.
import matplotlib.pyplot as plt

# Call the plot() function, to set the values we want to plot.
plt.plot([1,2,3,4])

# Set some other info on the graph, e.g. the labels on the x and y axes.
plt.xlabel('This is the x axis')
plt.ylabel('This is the y axis')

# Display the figure.
plt.show()