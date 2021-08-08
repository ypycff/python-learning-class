from netCDF4 import Dataset

# Create a Dataset (which has a root group, remember).
rootGroup = Dataset("myfile.nc", "w")

# netCDF defines the sizes of all variables in terms of "dimensions".
# So before you can create any variables, you must create the dimensions that they use.
#
# To create some Dimension objects in the root group. To create a Dimension object:
#   - Call createDimension() on a Dataset or Group object.
#   - Pass in the name of the dimension, as a string.
#   = Pass in the size of the dimension, as an integer (or 0 or None for an unlimited dimension, that you can append to).

# Let's create Dimension objects. 
level = rootGroup.createDimension("level", 0)
time  = rootGroup.createDimension("time", 0)
lat   = rootGroup.createDimension("lat", 73)
lon   = rootGroup.createDimension("lon", 144)

# All the Dimension objects are stored in a Python dictionary.
print("\nHere are all the Dimension objects:")
print(rootGroup.dimensions)

print("\nHere's just the 'level' Dimension object:")
print(rootGroup.dimensions["level"])

# You can get info about a Dimension object.
print("\nFor the lat Dimension, name is %s" % lat.name)
print("For the lat Dimension, current size is %d" % len(lat))
print("For the lat Dimension, isunlimited is %s" % lat.isunlimited())

rootGroup.close()