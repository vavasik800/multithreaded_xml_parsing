
PATTERN_FOR_HEADER = """<?xml version="1.0" encoding="utf-8"?>
<imp:Import xsi:type="imp:FullImport" createdAt="2013-08-17T10:41Z"
	dataType="DESTINATION" recordCount="3" transportSegment="SHIP"
	xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xmlns:dt="http://www.egis-otb.ru/datatypes/"
	xmlns:imp="http://www.egis-otb.ru/gtimport/" xmlns:onsi-stat="http://www.egis-otb.ru/data/onsi/stations/"
	xsi:schemaLocation="http://www.egis-otb.ru/gtimport/ ru.egisotb.import.xsd http://www.egis-otb.ru/data/onsi/stations/ ru.egisotb.data.onsi.stations.xsd
	http://www.egis-otb.ru/datatypes/ ru.egisotb.datatypes.xsd
	">
	
"""

PATTERN_FOR_FOOTER = """
</imp:Import>
"""

PATTERN_FOR_ENTRY = """
<entry sourceId="{id}" xsi:type="imp:ImportedEntry">
                    <data  name="Кижи" latitude="50,852458" longitude="48,878787" UTC="Europe/Moscow" 
		 nearestTown="Петрозаводск" shortLatName="Kzh" shortName="Кж" otiCode="3456789012"
		xsi:type="onsi-stat:ShipStation">
			<actualPeriod  from="2013-04-22T00:00Z" to="2023-04-20T00:00Z" xsi:type="dt:ImportDateTimePeriod"/>
			<countryCode value="Российская Федерация"
				xsi:type="dt:SimpleDictionaryValue" />
			<federalSubject value="Республика Карелия"
				xsi:type="dt:SimpleDictionaryValue" />
			<okato value="57218825003" xsi:type="dt:SimpleDictionaryValue" />
			<portType>true</portType>
		</data>
	</entry>
	
"""


def generate_xml(path_out_xml: str, count_entry: int):
    xml_doc = PATTERN_FOR_HEADER
    for i in range(count_entry):
        xml_doc += PATTERN_FOR_ENTRY.format(id=i)
    xml_doc += PATTERN_FOR_FOOTER
    with open(path_out_xml, 'w', encoding='utf-8') as file:
        file.write(xml_doc)
    return

generate_xml('test_big_xml_1000.xml', 1_000)