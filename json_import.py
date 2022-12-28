import json

# проверка что файл читается и имеет корректную структуру данных
def parseJS(json_file):
    struct = False
    with open(json_file,'r', encoding="utf-8") as jsfile:
        reader = json.load(jsfile)
        struct = True
        for key in reader:
            if not (key == 'phonebook'):
                struct = False

        for i in reader['phonebook']: 
            if not ((list(i.keys())[0])=='surname' and (list(i.keys())[1])=='name' and \
                (list(i.keys())[2])=='phone' and (list(i.keys())[3])=='description'):
                struct = False
    return struct

# формирование массива кортежей для записи в БД
def importJS(json_file):
    data_list=[]
    with open(json_file,'r', encoding="utf-8") as jsfile:
        reader = json.load(jsfile)

        for i in reader['phonebook']:
            t = ()
            t = (i['surname'],)
            t = t + (i['name'],)
            t = t + (i['phone'],)
            t = t + (i['description'],)
            data_list.append(t)
    return(data_list)


