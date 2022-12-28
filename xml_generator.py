def create(datalist):
    xml = '<?xml version="1.0" encoding="UTF-8"?>\n'
    xml += '<phonebook>\n'
    for d in datalist:
        xml += '    <record>\n'
        xml += '        <surname>{}</surname>\n'.format(d[1])
        xml += '        <name>{}</name>\n'.format(d[2])
        xml += '        <phone>{}</phone>\n'.format(d[3])
        xml += '        <description>{}</description>\n'.format(d[4])
        xml += '    </record>\n'
    xml += '</phonebook>\n'


    with open('data.xml','w', encoding="utf-8") as page:
        page.write(xml)
    return xml


