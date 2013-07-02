# coding: utf-8

import xml.etree.ElementTree as ET

tree = ET.parse('pretty-xml-sample.xml')
root = tree.getroot()

vehicle_journeys = root[6]

for journey in vehicle_journeys:
	print journey[3].text # journey ID
	print journey[7].text # timestamp
	print ''
