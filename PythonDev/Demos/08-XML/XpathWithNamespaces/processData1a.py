import xml.etree.ElementTree as ET

tree = ET.parse('data.xml')
root = tree.getroot()

ns = '{http://www.acme.com}'

calls = root.find(ns + 'Calls')

for call in calls.findall(ns + 'Call'):
    startTime = call.find(ns + 'StartTime')
    print(startTime.text)
