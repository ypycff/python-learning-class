from netCDF4 import Dataset
import numpy as np

# Create a Dataset and some dimensions, as before.
rootGroup = Dataset("myfile.nc", "w")
level = rootGroup.createDimension("level", 0)
time  = rootGroup.createDimension("time", 0)
lat   = rootGroup.createDimension("lat", 73)
lon   = rootGroup.createDimension("lon", 144)

# Create some 1-dimensional Variable objects, as before. 
times      = rootGroup.createVariable("time",  "f8", ("time",))
levels     = rootGroup.createVariable("level", "i4", ("level",))
latitudes  = rootGroup.createVariable("lat",   "f4", ("lat",))
longitudes = rootGroup.createVariable("lon",   "f4", ("lon",))

# Populate the latitude variable with data.
latitudes[:] = np.arange(-90, 91, 2.5)

# Let's do some slicing.
print(latitudes[70:])
print(latitudes[:3])
print(latitudes[3:10])  
print(latitudes[3:10:2])
print(latitudes[3::2])
print(latitudes[::2]) 

rootGroup.close()