from multi_readers import WorkWithXmlMultiProcess, write_txt


def main():
    path_file_xml = 'data/00000_2015_11_04_12_12_12_111.xml'
    path_out_dir = 'out/'
    a = WorkWithXmlMultiProcess(path_file_xml, write_txt, path_out_dir, 3)
    a.run()
    return


if __name__ == '__main__':
    main()
