# -*- coding: utf-8 -*-
from __future__ import absolute_import, unicode_literals
import os
from encoder import XML2Dict


def to_csv(source='pagseguro.xml', destination='pagseguro.csv'):
    source = os.path.join('.', source)
    destination = os.path.join('.', destination)
    file = open(source, encoding="ISO-8859-1")
    content = file.read()
    xml2dict = XML2Dict("ISO-8859-1")
    dct = xml2dict.parse(content)
    destination_file = open(destination, 'w')
    columns = ['Transacao_ID', 'Status', 'Cliente_Email', 'Data_Compensacao', 'Valor_Liquido']
    header = ','.join(columns)
    destination_file.write(header)

    def to_csv_line(item):
        values = [item.get(c, b'sem valor').decode().replace(',', '.') for c in columns if item]
        return ','.join(values)

    for item in dct['NewDataSet']['Table']:
        destination_file.write('\n' + to_csv_line(item))


if __name__ == '__main__':
    to_csv()


