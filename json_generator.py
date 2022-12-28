def create(datalist:list):
    json = '{\n'
    json +='    "phonebook": [\n'
    for d in datalist:
        json += '   {\n'
        json += '       "surname": "{}",\n'.format(d[1])
        json += '       "name": "{}",\n'.format(d[2])
        json += '       "phone": "{}",\n'.format(d[3])
        json += '       "description": "{}"\n'.format(d[4])        
        if datalist.index(d) == len(datalist)-1:
            json += '   }\n'
        else:
            json += '   },\n'    
    json +='    ]\n'
    json +='}'


    with open('data.json','w', encoding="utf-8") as page:
        page.write(json)
    return json