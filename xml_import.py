import xml.etree.cElementTree as ET

# проверка структуры файла
def parseXML(xml_file):
    tree = ET.parse(xml_file)
    root = tree.getroot()
    struct = True
    for elem in root:
        if not (elem[0].tag=="surname" and elem[1].tag == "name" and elem[2].tag == "phone" and elem[3].tag == "description"):
            struct = False
    return struct

# создание массива кортежей для записи в БД
def arrayXML(xml_file):
    tree = ET.parse(xml_file)
    root = tree.getroot()
    data_list =[]
    for elem in root:
        str_data=()
        for subelem in elem:
            t = subelem.text
            if not t:
                t=""
            str_data =str_data+ (t,)
        data_list.append(str_data)
    return data_list
        
                
                



# 
            

    # print('\nAll atributes:')
    # for elem in root:
    #     for subelem in elem:
    #         t = subelem.text
    #         if not t:
    #             t=""
    #         print(subelem.tag + '=' + t)
