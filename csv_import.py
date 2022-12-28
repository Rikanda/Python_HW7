import csv

# преобразование в список кортежей для загрузки в БД и одновременно проверка структуры
def parseCSV(csv_file):
    data_list=[]
    with open(csv_file,'r', encoding="utf-8") as csvfile:
        reader = csv.reader(csvfile)
        line_count = 0
        for row in reader:
            if line_count==0:
                if not (row[0]=='surname' and row[1]=='name' and row[2]=='phone' and row[3]=='description'):
                    data_list.append('Bad structure')
                    break
                line_count+=1
            else:
                str_data = tuple(row)
                data_list.append(str_data)
                line_count+=1
    return(data_list)


