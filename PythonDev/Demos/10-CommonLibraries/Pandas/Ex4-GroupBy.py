import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# Read a csv file, get a DataFrame back. The file contains reviews from customers at a fictional coffee store (different Branches across the UK).
data = pd.read_csv('TripAdvisorReviews.csv')
print(data)

# Group by Branch.
byBranch = data.groupby('Branch')

# Display statistcal info about the ServiceQuality for each Branch. 
print('\nServiceQuality per branch')
print('----------------------------------------------------')
for item in byBranch.ServiceQuality:
    print('\nServiceQuality stats for %s: ' % item[0])
    print('All: %s' % item[1].values)
    print('Num: %d' % item[1].count())
    print('Min: %d' % item[1].min())
    print('Max: %d' % item[1].max())
    print('Sum: %.2f' % item[1].sum())
    print('Avg: %.2f' % item[1].mean())

# Call describe() to describe the ServiceQuality for each Branch.	
print('\nServiceQuality full stats per branch')
print('----------------------------------------------------')
print(byBranch['ServiceQuality'].describe())

# Call min() to get the minimum value for ServiceQuality for each Branch.	
print('\nServiceQuality minimum values per branch')
print('----------------------------------------------------')
print(byBranch['ServiceQuality'].min())
	
# Call mean() to get the average value for ServiceQuality for each Branch.	
print('\nServiceQuality mean values per branch')
print('----------------------------------------------------')
print(byBranch['ServiceQuality'].mean())

