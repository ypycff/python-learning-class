from netCDF4 import Dataset
import numpy as np

# Create a Dataset and some dimensions, as before.
rootGroup = Dataset("myfile.nc", "w")
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

# Use Numpy universal functions to perform bulk operations on two variables.
print("Added:\n",      np.add(loTemperatures[0, 10, 20], hiTemperatures[0, 10, 20]))
print("Subtracted:\n", np.subtract(hiTemperatures[0, 10, 20], loTemperatures[0, 10, 20]))

sum = np.add(hiTemperatures[0, 10, 20], loTemperatures[0, 10, 20])
avg = np.divide(sum, 2)
print("Average:\n", avg)

rootGroup.close()