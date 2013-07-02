# coding: utf-8

import xml.etree.ElementTree as ET

tree = ET.parse('pretty-xml-sample.xml')
root = tree.getroot()