filepath = 'constitution_xml/english/ic.xml'
f = open(filepath, 'r')
while True:
    line = f.readline()
    if not line:
        break
    print 'this is a single line'
    print line
