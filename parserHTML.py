# Arquivo resposável por fazer o parse no html das páginas de notícias, bem como
# saber quais sites estão disponíveis;
# Cada função é responsável por um site;
# Todas as funções retornam o mesmo formato:
#   Uma lista de dicionários em que cada dicionario contem o link e o título da notícia;
#   o nome do respectivo site onde as notícias foram retiradas;

import requests
from bs4 import BeautifulSoup

# Dicionário e função resposáveis por proteger a função main
# Adicções de sites aqui não alterarão o código lá
available_sites = {'Globo.com': 1, 'cnn.com': 2}
def getNews(id):
    if id == 1:
        _list, name = globo()
    if id == 2:
        _list, name = cnn()

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
        dictAux = {'id': id, 'link': item.get('href'), 'titulo': item.get('title')}
        noticias.append(dictAux)
        id+=1
        #print(item.get('href') + '\n' +  item.get('title') + '\n\n')

    for item in noticias_menos_principais_aux:
        dictAux = {'id': id, 'link': item.get('href'), 'titulo': item.get('title')}
        id+=1
        noticias.append(dictAux)
        #print(item.get('href') + '\n' +  item.get('title') + '\n\n')

    # for item in noticias_raw2:
    #     if item.get('rel'):
    #         print(item.get('href') + '\n' +  item.get('title') + '\n\n')

    return noticias, 'globo.com'
    

def cnn():
    noticias = []
    return noticias, 'cnn.com'