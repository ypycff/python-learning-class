from netCDF4 import Dataset

# Create a Dataset and some dimensions, as before.
rootGroup = Dataset("myfile.nc", "w")
level = rootGroup.createDimension("level", 0)
time  = rootGroup.createDimension("time", 0)
lat   = rootGroup.createDimension("lat", 73)
lon   = rootGroup.createDimension("lon", 144)

# Create a multi-dimensional Variable. 
temperatures = rootGroup.createVariable("temp", "f4", ("time", "level", "lat", "lon"))

# Access an element in 4-dimensional space:
#  time  index = 0
#  level index = 10
#  lat   index = 20
#  long  index = 30
temperatures[0, 10, 20, 30] = 42.5

print("\nValues for time 0, level 10, latitude 20, longitude 30:")
print(temperatures[0, 10, 20, 30])

print("\nValues for time 0, level 10, latitude 20, all longitudes:")
print(temperatures[0, 10, 20, ::])

print("\nValues for time 0, level 10, all latitudes, longitude 30:")
print(temperatures[0, 10, ::, 30])

rootGroup.close()