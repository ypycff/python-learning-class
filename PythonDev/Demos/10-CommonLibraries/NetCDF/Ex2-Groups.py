from netCDF4 import Dataset

# Create a Dataset.
rootGroup = Dataset("myfile.nc", "w")

# Let's create 2 child groups underneath the root group. 
forecastsGroup = rootGroup.createGroup("forecasts")
analysesGroup  = rootGroup.createGroup("analyses")

print("\nRoot group's child groups:")
print(rootGroup.groups)

print("\nHere's just the 'forecasts' group:")
print(rootGroup.groups["forecasts"])

print("\nHere's just the 'analyses' group:")
print(rootGroup.groups["analyses"])

rootGroup.close()