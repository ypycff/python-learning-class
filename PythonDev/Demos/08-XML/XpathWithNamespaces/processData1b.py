import xml.etree.ElementTree as ET

tree = ET.parse('data.xml')
root = tree.getroot()

ns = '{http://www.acme.com}'

startTime_elements = root.findall( (ns + 'Calls') + 
                                   '/' +
                                   (ns + 'Call') +
                                   '/' + 
                                   (ns + 'StartTime') )
                      
for startTime_element in startTime_elements:
    print(startTime_element.text)


