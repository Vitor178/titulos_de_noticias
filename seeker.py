"""
=> Arquivo responsável por retornar todas as notícias que contenham uma palavra específica;
"""


def wordSeeker(noticias):
    _list = []
    palavra = getWord()

    for noticia in noticias:
        if palavra.lower() in noticia['titulo'].lower():
            _list.append(noticia)
            print('Título: %s\nLink: %s\n' % (noticia['titulo'], noticia['link']))
    # uma possível modificação seria salvar as noticias retornadas por esta função em um arquivo csv;
    # Para fazer isso seria necessário apenas substituir o print por uma chamada da função save_as_csv no arquivo csvMaker;

def getWord():
    print("Qual palavra deseja buscar?")
    palavra = input('>_')
    return palavra

