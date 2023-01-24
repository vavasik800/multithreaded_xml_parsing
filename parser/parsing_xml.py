from xml.etree import ElementTree as ET
from xml.etree.ElementTree import Element

from lxml import etree


def __con_dicts(dict1: dict, dict2: dict) -> dict:
    """
    Конкантинация словарей
    """
    return dict(list(dict1.items()) + list(dict2.items()))


def __tag_to_json(tag: Element):
    """
    Метод для получения всех значимых атрибутов листа.
    :param tag: тэг
    :return: tag_name - название тэга,
             json - все атрибуты с их значениями
    """
    tag_name, attributes = tag.tag, tag.attrib
    json = {key: attributes[key] for key in attributes if '{' not in key and '}' not in key}
    return tag_name, json


def __parsing_entry_xml(xml_entry: Element) -> dict:
    """
    Рекурсивный метод для обхода дерева xml и построение словаря одной записи.
    :param xml_entry: xml - элемент.
    :return: json-формат результата
    """
    response = {}
    tag_name, entry = __tag_to_json(xml_entry)  # получение названия тэга и всех атрибутов
    response[tag_name] = entry
    if len(xml_entry) == 0:
        # вызов для самого последнего листа дерева
        response[tag_name] = __con_dicts(response[tag_name], {'text': xml_entry.text or ''})
    else:
        for child in xml_entry:
            # рекурсивный вызов и дальнейший обход
            response[tag_name] = __con_dicts(response[tag_name], __parsing_entry_xml(child))
    return response


def parsing_xml(path_file_xml: str) -> tuple:
    """
    Парсинг xml - файла.
    :param path_file_xml: путь до файла xml
    :return: json - xml файла
    """
    tree = ET.parse(path_file_xml)
    root = tree.getroot()
    result = []
    for elem in root:
        result.append(__parsing_entry_xml(elem))
    return tuple(result)


def json_to_dict(json, name_tag=None) -> dict:
    """
    Рекурсивный метод для преобразования json - формата в одномерный словарь.
    :param json: json - формат
    :param name_tag: - имя тэга выше (для соединения полей)
    :return: одномерный словарь
    """
    response = {}
    for key in json:
        new_key = key if name_tag is None else f'{name_tag}_{key}'
        if type(json[key]) == dict:
            response = __con_dicts(response, json_to_dict(json[key], key))
        else:
            response[new_key] = json[key]
    return response


def parsing_elem_xml_str(entry_str: str):
    """

    :param entry_str:
    :return:
    """
    parser1 = etree.XMLParser(encoding="utf-8", recover=True)
    elem = ET.fromstring(entry_str, parser1)
    return __parsing_entry_xml(elem)

if __name__ == '__main__':
    str_element = """
    <entry sourceId="100" xsi:type="imp:ImportedEntry">
		<data  name="Санкт-Петербург" latitude="55,098765" longitude="55,098765" UTC="Europe/Moscow" 
		 nearestTown="Санкт-Петербург" shortLatName="Spb" shortName="Спб" otiCode="1234567890"
		xsi:type="onsi-stat:ShipStation">
			<actualPeriod  from="2013-04-22T00:00Z" to="2023-04-20T00:00Z" xsi:type="dt:ImportDateTimePeriod"/>
			<countryCode value="Российская Федерация"
				xsi:type="dt:SimpleDictionaryValue" />
			<federalSubject value="Санкт-Петербург"
				xsi:type="dt:SimpleDictionaryValue" />
			<okato value="40263561000" xsi:type="dt:SimpleDictionaryValue" />
			<portType>true</portType>
		</data>
                   </entry>
    """

