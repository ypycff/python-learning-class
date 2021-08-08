from netCDF4 import Dataset

# Create a Dataset and some dimensions, as before.
rootGroup = Dataset("myfile.nc", "w")
level = rootGroup.createDimension("level", 0)
time  = rootGroup.createDimension("time", 0)
lat   = rootGroup.createDimension("lat", 73)
lon   = rootGroup.createDimension("lon", 144)

# Let's create a multi-dimensional Variable. 
temperatures = rootGroup.createVariable("temp", "f4", ("time", "level", "lat", "lon"))
print(rootGroup.variables["temp"])

rootGroup.close()