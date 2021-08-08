from netCDF4 import Dataset
import numpy as np

# Create a Dataset and some dimensions, as before.
rootGroup = Dataset("myfile.nc", "w")
level = rootGroup.createDimension("level", 0)
time  = rootGroup.createDimension("time", 0)
lat   = rootGroup.createDimension("lat", 73)
lon   = rootGroup.createDimension("lon", 144)

# Create a multi-dimensional Variable. 
temperatures = rootGroup.createVariable("temp", "f4", ("time", "level", "lat", "lon"))

# You can fill a whole variable using np.full().
# E.g. for time[0], level[10], lat[20], set all 144 values to 42.5.
temperatures[0, 10, 20] = np.full(144, 42.5)
print(temperatures[0, 10, 20, ::])

# You can also fill part of a variable, using slice syntax.
temperatures[0, 10, 20, 0:72] = np.full(72, 99.9)
print(temperatures[0, 10, 20, ::])

# As well as np.full(), there are other functions you can use to populate a variable...
temperatures[0, 10, 20, 0:3]  = np.zeros(3)
temperatures[0, 10, 20, 3:6]  = np.ones(3)
temperatures[0, 10, 20, 6:9]  = np.random.random(3)          # Random numbers in range [0.0, 1.0).
temperatures[0, 10, 20, 9:12] = np.random.randint(75, 95, 3) # Random integers in range [75, 95).
print(temperatures[0, 10, 20, ::])

rootGroup.close()