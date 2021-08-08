# The netcdf4-python library enables you to read/write netCDF4 (and netCDF3) files.
# To use netcdf4-python, you must install it as follows (this also installs numpy and cftome):
#    pip install netCDF4
# This installs the netCDF4 package (in the directory [PYTHON_HOME]/lib/site-packages/netCDF4.).
# 
# For online docs, see: 
#    https://unidata.github.io/netcdf4-python/netCDF4/


# The netCDF4 package defines a Dataset class, your entrypoint into the netCDF API. 
# A Dataset is a collection of dimensions, groups, variables, and attributes
# which describe the meaning of data and relations.
 
from netCDF4 import Dataset

# To create (or read from) a netDCF file in Python, just create a Dataset object.
# The format parameter can be "NETCDF3_CLASSIC", "NETCDF3_64BIT_OFFSET", "NETCDF3_64BIT_DATA", "NETCDF4_CLASSIC", or "NETCDF4" (this is the default).
rootGroup = Dataset("myfile.nc", "w", format="NETCDF4")

# netCDF4 allows you to organise data into hierarchical groups (similar concept to directories).
# A group is a container of dimensions, variables, and attributes.
# A Dataset has a special group called the "root group". You can get info about it as follows:
print("\nHere's info about the Dataset's root group:")
print(rootGroup) 

# Close the netcdf file.
rootGroup.close()