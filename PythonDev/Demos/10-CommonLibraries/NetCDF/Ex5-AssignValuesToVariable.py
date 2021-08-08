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

# Create a Numpy data array holding latitude data, and assign into the latitudes variable.
latitudeData = np.arange(-90, 91, 2.5)
latitudes[:] = latitudeData
print("\nlatitudes variable length %d" % len(latitudes))
print("latitudes variable data:\n", latitudes[:])

# Create a Numpy data array holding longitude data, and assign into the longitudes variable.
longitudeData =  np.arange(-180, 180, 2.5)
longitudes[:] = longitudeData
print("\nlongitudes variable length %d" % len(longitudes))
print("longitudes variable data:\n", longitudes[:])

rootGroup.close()