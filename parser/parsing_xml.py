from xml.etree import ElementTree as ET
from xml.etree.ElementTree import Element


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


