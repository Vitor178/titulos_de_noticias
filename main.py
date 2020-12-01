# Arquivo responsável por realizar a interação com o usuário

import argparse
import parserHTML
import csvMaker


def main():
    #parser = argparse.ArgumentParser(description='Salve as notícias de hoje em um arquivo csv')
    
    print('\nEscolha um site para retornar as notícias:')
    # esta verificação no dicionario permite que adições de novos sites não 
    # cause a necessidade de mudanças neste código
    for name in parserHTML.available_sites.keys():
        print('Para %s digite %s' % (name, parserHTML.available_sites.get(name)))

    value = int(input(">_ "))
    _list, siteName = parserHTML.getNews(value)

    csvMaker.save_as_CSV(_list, siteName)
    print('ok!')


if __name__ == "__main__":
    main()