import processamento
import plotmodule
import arquivos

def gerente():
    while True:
        print("\n")
        print("==============================================================================\n")
        print("                                                                      MENU INICIAL\n")
        print("==============================================================================\n")
        print("\n Digite 1 para a consulta do top 10 de média de vendas por plataforma para uma determinada região.\n",
              "Digite 2 para a consulta da média de vendas de acordo com um determinado gênero dos jogos vendidos nas regiões.\n",
              "Digite 3 para a consulta da média das vendas globais por ano, baseadas em um determinado intervalo de anos e um gênero.\n",
              "Digite 4 para a consulta da quantidade de jogos de acordo com os “X” maiores gêneros num intervalo de anos.\n",
              "Digite 5 para a consulta da vendas globais de jogos de cada plataforma de uma determinada publicadora.\n",
              "Digite 6 para a consulta da relação top “X” de jogos das vendas na região NA e EU.\n",
              "Digite 7 para a consulta de quais as 10 plataformas que têm mais jogos de um determinado gênero.\n",
              "Digite 8 para cadastrar um novo usuário.\n",
              "Digite 9 para remover um usuário.\n",
              "Digite 0 para sair.\n")
        busca = input()
        if busca == '1':
            print("\n")
            print("==============================================================================\n")
            print("                                                                      BUSCA 3\n")
            print("==============================================================================\n")
            plot = processamento.chamada_3()
            if plot != None:
                plotmodule.plot_3(plot[0], plot[1], plot[2])
        elif busca == '2':
            print("\n")
            print("==============================================================================\n")
            print("                                                                      BUSCA 4\n")
            print("==============================================================================\n")
            plot = processamento.chamada_4()
            if plot != None:
                plotmodule.plot_4(plot[0], plot[1], plot[2])
        elif busca == '3':
            print("\n")
            print("==============================================================================\n")
            print("                                                                      BUSCA 5\n")
            print("==============================================================================\n")
            plot = processamento.chamada_5()
            if plot != None:
                plotmodule.plot_5(plot[0], plot[1], plot[2])
        elif busca == '4':
            print("\n")
            print("==============================================================================\n")
            print("                                                                      BUSCA 6\n")
            print("==============================================================================\n")
            plot = processamento.chamada_6()
            if plot != None:
                plotmodule.plot_6(plot[0], plot[1], plot[2], plot[3])
        elif busca == '5':
            print("\n")
            print("==============================================================================\n")
            print("                                                                      BUSCA 7\n")
            print("==============================================================================\n")
            plot = processamento.chamada_7()
            if plot != None:
                plotmodule.plot_7(plot[0], plot[1], plot[2])
        elif busca == '6':
            print("\n")
            print("==============================================================================\n")
            print("                                                                      BUSCA 8\n")
            print("==============================================================================\n")
            plot = processamento.chamada_8()
            if plot != None:
                plotmodule.plot_8(plot[0], plot[1], plot[2])
        elif busca == '7':
            print("\n")
            print("==============================================================================\n")
            print("                                                                      BUSCA 12\n")
            print("==============================================================================\n")
            plot = processamento.chamada_12()
            if plot != None:
                plotmodule.plot_12(plot[0], plot[1], plot[2])
        elif busca == '8':
            print("\n")
            print("==============================================================================\n")
            print("                                                                      CADASTRO\n")
            print("==============================================================================\n")
            arquivos.criar_arquivo()
        elif busca == '9':
            checa = arquivos.exclui()
            if checa == 1:
                return
        elif busca == '0':
            False
            break 
        else:
            print("Comando inválido.")

def funcionario():
    while True:
        print("\n")
        print("==============================================================================\n")
        print("                                                                      MENU INICIAL\n")
        print("==============================================================================\n")
        print("\n Digite 1 para a consulta da média das vendas globais por ano, baseadas em um determinado intervalo de anos e um gênero.\n",
              "Digite 2 para a consulta da relação top “X” de jogos das vendas na região NA e EU.\n",
              "Digite 0 para sair.\n")
        busca = input()
        if busca == '1':
            print("\n")
            print("==============================================================================\n")
            print("                                                                      BUSCA 5\n")
            print("==============================================================================\n")
            plot = processamento.chamada_5()
            if plot != None:
                plotmodule.plot_5(plot[0], plot[1], plot[2])
        elif busca == '2':
            print("\n")
            print("==============================================================================\n")
            print("                                                                      BUSCA 8\n")
            print("==============================================================================\n")
            plot = processamento.chamada_8()
            if plot != None:
                plotmodule.plot_8(plot[0], plot[1], plot[2])
        elif busca == '0':
            False
            break 
        else:
            print("Comando inválido.")
