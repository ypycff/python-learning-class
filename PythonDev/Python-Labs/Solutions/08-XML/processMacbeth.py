import xml.etree.ElementTree as ET

def printElements(message, elements):
    print("\n%s" % message)
    for e in elements:
        print("\t%s" % e.text)

# Load an XML document and get the root element, i.e. <PLAY>.
tree = ET.parse("Macbeth.xml")
root = tree.getroot()

playTitle = root.findall("./TITLE[1]")
printElements("Title of the play", playTitle)

personae = root.findall(".//PERSONA")
printElements("All the personae", personae)

titles = root.findall(".//SCENE/TITLE")
printElements("Titles for all the scenes", titles)

duncanLinesOfSpeeches = root.findall(".//SPEECH[SPEAKER='DUNCAN']/LINE")
printElements("All the lines of speech by Duncan", duncanLinesOfSpeeches)
