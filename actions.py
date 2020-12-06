"""
=> Arquivo responsável por manter todas as ações disponíveis;
=> Este arquivo será modificado quando uma nova ação for adicionada;
"""
import csvMaker
import seeker

available_actions = {'salvar as noticias em um arquivo csv': 1,
                     'buscar notícias contendo uma palavra específica': 2}

def chooseAction(id, noticias, siteName):
    if id == 1:
        csvMaker.save_as_CSV(noticias, siteName)
    if id == 2:
        seeker.wordSeeker(noticias)
      