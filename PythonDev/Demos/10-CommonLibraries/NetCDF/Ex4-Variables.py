from netCDF4 import Dataset

# Create a Dataset and some dimensions, as before.
rootGroup = Dataset("myfile.nc", "w")
level = rootGroup.createDimension("level", 0)
time  = rootGroup.createDimension("time", 0)
lat   = rootGroup.createDimension("lat", 73)
lon   = rootGroup.createDimension("lon", 144)

# To store and manipulate data in netCDF, you must create a Variable object.
#
# A Variable object:
#  - Is similar to a Numpy array.
#  - Can be 1-dimensional or multi-dimensional.
#  - Holds a designated data type (all values in a Variable are the same type).
#
# To create a Variable object:
#   - Call createVariable() on a Dataset or Group object.
#   - Pass in the name of the dimension, as a string.
#   - Pass in the data type for values in the variable, as a string.
#     Valid data types are "f4", "f8", "i1", "i2", "i4", "i8", "u1", "u2", "u4", "u8", "S1".
#   = Pass in a tuple, specifying the names of the dimension(s) along which the variable's values will be placed.

# Let's create some 1-dimensional Variable objects. 
times      = rootGroup.createVariable("time",  "f8", ("time",))
levels     = rootGroup.createVariable("level", "i4", ("level",))
latitudes  = rootGroup.createVariable("lat",   "f4", ("lat",))
longitudes = rootGroup.createVariable("lon",   "f4", ("lon",))

# All the Variable objects are stored in a Python dictionary.
print("\nHere are all the Variables:")
print(rootGroup.variables)

print("\nHere's just the 'level' Variable object:")
print(rootGroup.variables["level"])

# You can get info about a Variable object.
print("\nFor the lat Variable, shape is %s" % latitudes.shape)
print("For the lat Variable, data type of values is %s" % latitudes.dtype)

rootGroup.close()