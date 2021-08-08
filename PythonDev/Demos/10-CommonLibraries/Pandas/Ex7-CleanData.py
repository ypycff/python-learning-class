import pandas as pd

# Read Excel spreadsheet, get a DataFrame back.
data = pd.read_excel('TripAdvisorReviews.xlsx')

print('\nBranches initially:')
print(data.Branch.values)

# For all items where Branch is 'Moorgate', change Branch to 'City', and set all ratings to infeasibly high numbers (10, 20, and 30 respectively).
predicate = (data.Branch == 'Moorgate')
data.loc[predicate, ('Branch', 'ServiceQuality', 'FoodQuality', 'Cleanliness')] = ('City', 10, 20, 30)

# Delete all items where Branch is Cardiff :-P 
data = data[data.Branch != 'Cardiff']

# Convert all Branch names to uppercase.
data.Branch = data.Branch.apply(lambda b: b.upper())

# After all that work, reset the indexes.
data = data.reset_index()

print('\nBranches finally:')
print(data.Branch.values)

print('\nAll data finally:')
print(data)
