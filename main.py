# Arquivo responsável por realizar a interação com o usuário

import parserHTML
import actions


def main():

    while True:
        print('\nEscolha a ação desejada:')
        for acao in actions.available_actions.keys():
            print('Para %s digite %s' % (acao, actions.available_actions.get(acao)))
        op1 = int(input(">_ "))
        if op1 not in actions.available_actions.values():
            print("opção escolhida não pertece as opções disponíveis!")
        else:
            break
    
    while True:
        print('\nEscolha o site para realizar a ação escolhida:')
        for name in parserHTML.available_sites.keys():
            print('Para %s digite %s' % (name, parserHTML.available_sites.get(name)))
        print('Para todos os anteriores digite %s' % (0))
        op2 = int(input(">_ "))
        if op2 not in parserHTML.available_sites.values() and op2 != 0:
            print("opção escolhida não pertece as opções disponíveis!")
        else:
            break

    noticias, siteName = parserHTML.getNews(op2)

    actions.chooseAction(op1, noticias, siteName)


if __name__ == "__main__":
    main()