import xml.etree.ElementTree as ET

def findAllWithNamespace(r, ns, xpath):
    xpathSteps = xpath.split('/')
    xpathStepsWithNs = [ '{' + ns + '}' + s  for s in xpathSteps ]
    xpathWithNs = '/'.join(xpathStepsWithNs)
    return r.findall(xpathWithNs)

tree = ET.parse('data.xml')
root = tree.getroot()

elems = findAllWithNamespace(
            root, 
            'http://www.acme.com', 
            'Calls/Call/StartTime')

for elem in elems:
    print(elem.text)
    