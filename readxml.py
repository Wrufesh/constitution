import xml.etree.ElementTree as ET

filepath = 'constitution_xml/english/ic.xml'
test_file = 'sample.xml'
# tree = ET.parse(test_file)
# root = tree.getroot()

# for child in root:
# 	print child.text
tree = ET.parse(filepath)
root = tree.getroot()

for child in root:
    for txt in child.iter('text'):
        x = list(txt)
        if len(x) > 0:
            li = ET.tostringlist(txt)
            string = ''.join(li[7:-2])
            print string
        else:
        	print 'this is a plain text'
    print 'pagenumber', child.get('number')


# f = open(filepath, 'r')
# while True:
#     line = f.readline()
#     if not line:
#         break
#     print 'this is a single line'
#     print line
