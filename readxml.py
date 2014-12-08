#!/usr/bin/python

import xml.etree.ElementTree as ET
import re

filepath = 'constitution_xml/english/ic.xml'
test_file = 'sample.xml'
tree = ET.parse(filepath)
root = tree.getroot()

# returns whole inner element including tags (works only for text type element)


def get_contained_data_in_str(element):
    li = ET.tostringlist(element)
    string = ''.join(li[7:-2])
    return string

# Checks whether starting and ending of the string is <b> and </b>
# respectively.


def is_bold_bounded(string):
    if re.match(r'^(|[ ]+|\n)<b>.*\</b>(|[ ]+|\n)$', string):
        return True
    else:
        return False


def inner_text_without_tag(element):
    li = []
    for chd in element.itertext():
        if is_superscript(element) != True:
            li.append(chd)
    allstr = ''.join(li)
    return allstr


def is_superscript(element):
    width = element.get('width')
    height = element.get('height')
    if int(width) < 24 and int(height) < 15:
        return True
    else:
        return False


article_number = None
article = None
parent_article = None


for child in root:
    for i, txt in enumerate(child):
        x = list(txt)
        # if length is equal to 1 then <text> element has only one child
        # element
        if len(x) == 1:
            string = get_contained_data_in_str(txt)
            if is_bold_bounded(string):
                s = txt[0].text
                if re.match(r'^(Part|PART|Schedule)', s):
                    print child[i][0].text
                    loop = True
                    counter = 1
                    lis = []
                    while loop:
                        inner_text = inner_text_without_tag(child[i+counter])
                        if re.match(r'^[ ]*[0-9]+', inner_text) or int(child[i+counter].get('left')) < 200:
                            a = ''.join(lis)
                            print a
                            loop = False
                        else:
                            lis.append(inner_text)
                            counter = counter + 1



                # Now check pure bold one upper element part or not
                # use enumerate()
        # else:
    #         print 'this is a plain text'
    # print 'pagenumber', child.get('number')

# Human Error in source pdf
# There are two same major clause number (13)(28)(32)(32)
# After major-clause no 36..it is continued by 36A..36B..
# We have a problem here.. b
