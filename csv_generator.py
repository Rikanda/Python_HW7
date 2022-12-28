def create(datalist):
    csv = 'surname;name;phone;description\n'
    for d in datalist:
        csv += '{}\n'.format(';'.join(str(el) for el in d[1::]))

    with open('data.csv','w', encoding="utf-8") as page:
        page.write(csv)
    return csv