import pandas as pd 
import numpy.random as npr
import time

# Set a seed for Numpy random number generator.
npr.seed(int(time.time()))

# All branches.
branches = ['Moorgate', 'Swansea', 'Paris', 'Cardiff', 'NY']

# Create 20 sets of random review data.
random_branches   = [branches[npr.randint(low=0,high=len(branches))] for i in range(20)]
random_sq_ratings = npr.randint(low=1,high=6,size=20)   # 20 random service quality ratings
random_fq_ratings = npr.randint(low=1,high=6,size=20)   # 20 random food quality ratings
random_c_ratings  = npr.randint(low=1,high=6,size=20)   # 20 random cleanliness ratings

# Zip the random fields into a list of 'Branch', 'ServiceQuality', 'FoodQuality', 'Cleanliness' rows.
random_reviews = list(zip(random_branches, random_sq_ratings, random_fq_ratings, random_c_ratings))	
print('Random reviews:\n%s\n' % random_reviews)

# Write data to an Excel spreadsheet.
df = pd.DataFrame(data=random_reviews, columns=['Branch', 'ServiceQuality', 'FoodQuality', 'Cleanliness'])
df.to_excel('TripAdvisorReviews.xlsx', index=False)
print('All data saved to TripAdvisorReviews.xlsx')

# Now group data by Branch, and write each branch to a separate sheet in an Excel spreadsheet.
# We'll use a Pandas Excel writer to enable us to do multiple writes to the same spreadsheet.
byBranch = df.groupby('Branch')
excelWriter = pd.ExcelWriter('TripAdvisorReviewsMultipleSheets.xlsx')
for item in byBranch:
    # item is a tuple...
    # item[0] is a Branch value, e.g. Swansea - this is the name of the sheet we want to create in the Excel sheet.
    # item[1] is a DataFrame containing all the data for that branch - this is the data we want to write to the Excel sheet.
    item[1].to_excel(excelWriter, sheet_name=item[0])
excelWriter.save()
print('By-branch data saved to separate sheets in TripAdvisorReviewsMultipleSheets.xlsx')
