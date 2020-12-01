# Arquivo responsável por receber as informações das notícias e salva-lás 
# em um arquivo no formato csv;

from datetime import date
import csv

def save_as_CSV(_list, siteName):
    fileName = getFileName(siteName)
    columns = ['id', 'titulo', 'link']

    with open(fileName, 'w') as _file:
        writer = csv.DictWriter(_file, fieldnames=columns)
        writer.writeheader()
        for item in _list:
            writer.writerow(item)

def getFileName(siteName):
    today = date.today().strftime("%d-%b-%Y")
    return '%s_%s.csv' % (siteName, today)
