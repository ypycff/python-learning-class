import pandas as pd
import glob

# Read all the CSV files in the folder "mydatafolder".
filenames = glob.glob("mydatafolder/*.csv")

# Create an empty list. Eventually this will hold a list of DataFrame objects (one DataFrame per file).
dataframes = []

for filename in filenames:
    # Read the data from a file into a new DataFrame object.
    df = pd.read_csv(filename, names=['fname','sname','region','salary'])
    
    # Add a column to the DataFrame we just created, indicating the name of the file where this data came from.
    df['SourceFilename'] = filename
    
    # Append the DataFrame object to the list of all DataFrames.
    dataframes.append(df)


# Concatenate all the DataFrame objects into a single unified DataFrame. (Ignore the index column for each contributory DataFrame).
unified_dataframe = pd.concat(dataframes, ignore_index=True)

# Let's see the results :-)
print(unified_dataframe)