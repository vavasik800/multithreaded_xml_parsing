import os
from multiprocessing import Process

from parsing_xml import parsing_xml, json_to_dict


class WorkWithXmlMultiProcess:
    """
    Класс для запуска множества потоков.
    """
    def __init__(self, path_in_file: str, working_func, path_out_dir: str = 'out/', count_threads: int = 2):
        """
        Инициализация класса.
        :param path_in_file: путь до входного файла xml.
        :param working_func: используемая в обработке функция.
        :param path_out_dir: путь выходного каталога.
        :param count_threads: количесто потоков.
        """
        if not os.path.exists(path_out_dir):
            os.makedirs(path_out_dir)
        self.path_out_dir = path_out_dir
        self.in_file = path_in_file
        self.count_threads = count_threads
        self.header = None
        self.processes = []
        self.working_function = working_func

    def __run_processes(self):
        """
        Запуск процессов.
        """
        for p in self.processes:
            p.start()
        for p in self.processes:
            p.join()
        self.processes = []
        return

    def run(self):
        """
        Основной метод запука процессов.
        :return:
        """
        # обход файла и последующий запуск процессов
        for index, entry in enumerate(parsing_xml(self.in_file)):
            if index % self.count_threads == 0:
                self.__run_processes()
            self.processes.append(Process(target=self.working_function,
                                          args=(json_to_dict(entry), self.path_out_dir,),
                                          daemon=True))
        self.__run_processes()
        return


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



