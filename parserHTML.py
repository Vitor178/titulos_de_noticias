"""
=> Arquivo responsável por fazer o parse no html das páginas de notícias, bem como
saber quais sites estão disponíveis para tal parse;
=> Cada função é responsável por um site;
=> Todas as funções retornam o mesmo formato:
    Uma lista de dicionários contendo um id, o link para a notícia e o título da notícia;
    O nome do site onde as notícias foram retiradas;
"""

import requests
from bs4 import BeautifulSoup

# Dicionário e função responsáveis por proteger a função main
# Adições de sites aqui não alterarão o código lá
available_sites = {'Globo.com': 1, 'cnn.com': 2}
def getNews(id):
    if id == 1:
        _list, name = globo()
    if id == 2:
        _list, name = uol()
    if id == 0:
        _list, name = all()

    return _list, name    


def globo():
    noticias = []
    page = requests.get('https://www.globo.com/').content
    soup = BeautifulSoup(page.decode('utf8'), 'html.parser')

    noticias_principais = soup.find_all(class_="hui-premium__link")
    noticias_menos_principais_aux = soup.find_all(class_="hui-premium__related-link")
    
    #noticias_raw2 = soup.find_all(class_="hui-highlight__link")
    id = 0
    for item in noticias_principais:
        dictAux = {'id': id, 'link': item.get('href'), 'titulo': item.get('title').replace('\n',' ')}
        noticias.append(dictAux)
        id+=1
        #print(item.get('href') + '\n' +  item.get('title') + '\n\n')

    for item in noticias_menos_principais_aux:
        dictAux = {'id': id, 'link': item.get('href'), 'titulo': item.get('title').replace('\n',' ')}
        id+=1
        noticias.append(dictAux)
        #print(item.get('href') + '\n' +  item.get('title') + '\n\n')

    # for item in noticias_raw2:
    #     if item.get('rel'):
    #         print(item.get('href') + '\n' +  item.get('title') + '\n\n')

    return noticias, 'globo.com'
    

def uol():
    noticias = []
    page = requests.get('https://noticias.uol.com.br/').content
    soup = BeautifulSoup(page.decode('utf8'), 'html.parser')

    principais = soup.find_all(class_="title-box")
    menos_principais = soup.find_all(class_="thumbnails-wrapper")
    
    id = 0
    for item in principais:
        dictAux = {'id': id, 'link': item.get('href'), 'titulo': item.find('h2').text.replace('\n',' ')}
        noticias.append(dictAux)
        id+=1

    for item in menos_principais:
        dictAux = {'id': id, 'link': item.find('a').get('href'), 'titulo': item.find('h3').text.replace('\n',' ')}
        noticias.append(dictAux)
        id+=1
    return noticias, 'noticias.uol.com.br'


def all():
    noticias = []
    for id in available_sites.values():
        listAux, _ = getNews(id) 
        noticias.extend(listAux)
    return noticias, 'all'
