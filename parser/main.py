from parsing_xml import parsing_xml, json_to_dict


def write_txt(dict_entry: dict, name_file_dir: str = None):
    """
    Запись данных в txt - файл
    :param dict_entry:
    :return:
    """
    name_file_out = f'{name_file_dir}{dict_entry["entry_sourceId"]}.txt'
    with open(name_file_out, 'w', encoding='cp1251') as file:
        for key, value in dict_entry.items():
            file.write(f'{key}  -   {value}\n')
    return


def work_with_file(path_file_xml: str, out_files_dir: str):
    """
    Работа с xml - файлом.
    :param path_file_xml: путь до xml файла.
    :return:
    """
    json_data = parsing_xml(path_file_xml)
    for entry in json_data:
        new_dict = json_to_dict(entry)
        write_txt(new_dict, name_file_dir=out_files_dir)
    return


def main():
    path_file_xml = 'data/00000_2015_11_04_12_12_12_111.xml'
    path_out_dir = 'out/'
    work_with_file(path_file_xml, path_out_dir)
    return


if __name__ == '__main__':
    main()
