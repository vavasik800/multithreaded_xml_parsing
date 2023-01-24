import glob
import os
import time

from multi_readers import WorkWithXmlMultiProcess, write_txt


def main():
    # path_file_xml = 'data/00000_2015_11_04_12_12_12_111.xml'
    path_file_xml = 'test_big_xml.xml'
    path_out_dir = 'out/'
    a = WorkWithXmlMultiProcess(path_file_xml, write_txt, path_out_dir, 1000)
    print('Считываем весь файл')
    start = time.time()
    a.run()
    finish = time.time()
    print("Время выполнения функции, сначала считав весь файл - ", start - finish)
    # time.sleep(3)
    # files = glob.glob(path_out_dir + '*')
    # for f in files:
    #     os.remove(f)
    # time.sleep(3)
    # # print('Считываем файл последовательно')
    # # start = time.time()
    # # a.run()
    # # finish = time.time()
    # # print("Время выполнения функции, читая файл последовательно - ", start - finish)
    # # for f in files:
    # #     os.remove(f)
    # # time.sleep(3)
    # print('Без потоков')
    # start = time.time()
    # a.run_2()
    # finish = time.time()
    # print("Время выполнения функции, без многопоточечности ", start - finish)
    return


if __name__ == '__main__':
    main()
