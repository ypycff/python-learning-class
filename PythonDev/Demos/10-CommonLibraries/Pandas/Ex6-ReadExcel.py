import pandas as pd

# Read an Excel spreadsheet, get a DataFrame back.
data = pd.read_excel('TripAdvisorReviews.xlsx')

print("\nData description:\n%s" % data.describe())
print("\nData:\n%s"             % data)

# You can now use DataFrame as before...
byBranch = data.groupby('Branch')
for item in byBranch['ServiceQuality']:
    print('\nServiceQuality stats for %s: ' % item[0])
    print('All: %s' % item[1].values)
    print('Num: %d' % item[1].count())
    print('Min: %d' % item[1].min())
    print('Max: %d' % item[1].max())
    print('Sum: %.2f' % item[1].sum())
    print('Avg: %.2f' % item[1].mean())
	
