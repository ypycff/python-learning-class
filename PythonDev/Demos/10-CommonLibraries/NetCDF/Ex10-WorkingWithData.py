from netCDF4 import Dataset
import numpy as np

# Create a Dataset and some dimensions, as before.
rootGroup = Dataset("myfile.nc", "w")
level = rootGroup.createDimension("level", 0)
time  = rootGroup.createDimension("time", 0)
lat   = rootGroup.createDimension("lat", 73)
lon   = rootGroup.createDimension("lon", 144)

# Create a multi-dimensional Variable and fill with some values.
temperatures = rootGroup.createVariable("temp", "f4", ("time", "level", "lat", "lon"))
temperatures[0, 10, 20] = np.random.randint(-5, +25, 144)
print("Original temperatures:\n", temperatures[0, 10, 20])

# Use Numpy universal functions to perform bulk operations.
print("Added 10:\n",         np.add(temperatures[0, 10, 20], 10))
print("Subtracted 10:\n",    np.subtract(temperatures[0, 10, 20], 10))
print("Multiplied by 10:\n", np.multiply(temperatures[0, 10, 20], 10))
print("Divided by 10:\n",    np.divide(temperatures[0, 10, 20], 10))
print("Squared:\n",          np.power(temperatures[0, 10, 20], 2))

rootGroup.close()