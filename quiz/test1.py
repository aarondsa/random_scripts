#script to extract data from an xml file using python
from lxml import etree
import urllib2
from xml.dom.minidom import parse


document = open('storage.txt')
instance = etree.parse(document)
print document
document.close()

print document
print instance


root = instance.getroot()
print root.tag
child = root.findall('answer')
print child
"""

#make a variable and fill it with file contents
pig = open('storage.txt')
#parse the file contents
#from now on, if you want to do something to the xml..."data."something something something
data = parse(pig)


#as in here: data.getElementsByTagName
tag = data.getElementsByTagName('answer')[1].toxml()
print tag
print '---------------------------------'

finaltag = tag.replace('<answer>', '').replace('</answer>', '')
print finaltag
print '---------------------------------'

i = 0
while i < 2:
    thetag = data.getElementsByTagName('answer')[i].toxml()
    print thetag
    i = i + 1

print '---------------------------------'

bill = data.childNodes
print 'bill'
print bill

print '-----------------------------------'
for node in data.childNodes:
    print node

print '---------------------------------'
for node in bill:
    print node,
"""
