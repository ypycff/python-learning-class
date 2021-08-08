import xml.etree.ElementTree as ET

# Load an XML document and get the root element, i.e. <Company>.
tree = ET.parse("Company.xml")
root = tree.getroot()

# Print the element's tag name, attributes, and text content.
print("Root tag name: %s" % root.tag)
print("Root tag attributes: %s" % root.attrib)
print("Root tag text: %s" % root.text)

# Iterate through all child elements of root.
print("\nAll children of root:")
for child in root:
    print("  %s, %s, %s" % (child.tag, child.attrib, child.text))

# Index to the employee 1 and get its 2nd child element.
emp1Sal = root[1][2]
print("For employee[1], %s is %s" % (emp1Sal.tag, emp1Sal.text))

# Find the first child <Employee> element of root.
firstEmp = root.find("Employee")
print("\nTelephone numbers for first employee:")
for tel in firstEmp.findall("Tel"):
    print("  %s" % tel.text)

# Iterate through all descendant <Salary> elements of root.
print("\nSalaries for all employees:")
for sal in root.iter('Salary'):
    print("  %s" % sal.text)
