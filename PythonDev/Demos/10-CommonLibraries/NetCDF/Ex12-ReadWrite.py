from netCDF4 import Dataset
import numpy as np

# Create a Dataset and some dimensions, as before.
rootGroup = Dataset("myTemps.nc", "w", persist=True)
level = rootGroup.createDimension("level", 0)
time  = rootGroup.createDimension("time", 0)
lat   = rootGroup.createDimension("lat", 73)
lon   = rootGroup.createDimension("lon", 144)

# Create a multi-dimensional Variable and fill with some "low temperature" values.
loTemperatures = rootGroup.createVariable("lotemp", "f4", ("time", "level", "lat", "lon"))
loTemperatures[0, 10, 20] = np.random.randint(0, +5, 144)
print("Low temperatures:\n", loTemperatures[0, 10, 20])

# Create a multi-dimensional Variable and fill with some "high temperature" values.
hiTemperatures = rootGroup.createVariable("hitemp", "f4", ("time", "level", "lat", "lon"))
hiTemperatures[0, 10, 20] = np.random.randint(+10, +30, 144)
print("High temperatures:\n", hiTemperatures[0, 10, 20])

rootGroup.close()

rootGroupReadIn = Dataset("myTemps.nc", "r")
print("\nDimensions read in:\n",        rootGroupReadIn.dimensions)
print("\nVariables read in:\n",         rootGroupReadIn.variables)
print("\nLow temperatures read in:\n",  rootGroupReadIn.variables["lotemp"][0, 10, 20])
print("\nHigh temperatures read in:\n", rootGroupReadIn.variables["hitemp"][0, 10, 20])


