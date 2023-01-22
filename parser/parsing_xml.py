from xml.etree import ElementTree as ET
from xml.etree.ElementTree import Element
from typing import List


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
        response[tag_name] = dict(list(response[tag_name].items()) + list({'text': xml_entry.text or ''}.items()))
    else:
        for child in xml_entry:
            # рекурсивный вызов и дальнейший обход
            response[tag_name] = dict(list(response[tag_name].items()) + list(__parsing_entry_xml(child).items()))
    return response


def parsing_xml(path_file_xml: str) -> List[dict]:
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
    return result


