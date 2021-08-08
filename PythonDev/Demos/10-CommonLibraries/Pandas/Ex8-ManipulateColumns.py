import pandas as pd

# Read Excel spreadsheet, get a DataFrame back.
data = pd.read_excel('TripAdvisorReviews.xlsx')

# Change the name of the colums.
data.columns = ['Location', 'Service', 'Food', 'Cleanliness']

# Add a new column called 'Reviewer', and set its value to 'Anon' for each row.
data['Reviewer'] = 'Anon'

# Add a new column called 'Recommend?', and set its value to True or False for each row.
data['Recommend?'] = [n % 3 == 0 for n in range(20)]

print(data)
