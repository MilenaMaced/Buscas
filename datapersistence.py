import plotmodule
import arquivos

def ler_persistir(parametros):#função que auxilia a persistência de buscas realizadas
    persistir = arquivos.retorna_user()
    arquivo = open("{}.txt".format(persistir), "r")#lemos primeiramente o arquivo o qual o usuário está logado
    lista = []
    lista_pronta = []
    dados = []
    x = []
    y = []
    for h in arquivo:
        recebe = h.split('\n')#cada linha do arquivo será separada como uma unica string em uma lista
        del(recebe[len(recebe)-1])#deletamos os \n, para que eles não sejam armazenados
        dados.append(recebe)#e então colocamos em uma lista
    arquivo.close()#não podemos esquecer de fechar o arquivo depois que usá-lo
    if (len(dados)) != 1:#verificamos se há mais de uma linha no arquivo do usuario. Se houver, significa que há histórico para ser analisado. 
        dados = dados[1:]#não iremos analisar a posição 0 do arquivo, pois se trata apenas dos dados cadastrais
        for t in range(len(dados)):
            for v in range(len(dados[t])):
                separar = dados[t][v].split(' ')#iremos separar cada a linha por espaço. A cada espaço, uma nova lista surge
                lista.append(separar)#e então colocamos tudo em uma nova lista
        for k in range(len(lista)):
            for i in range(len(lista[k])):
                novos = lista[k][i].strip().split(',')#agora, retiramos elementos indesejáveis com a funçã strip, e separamos cada dado pela ,
                lista_pronta.append(novos)#e agora temos uma lista com todo o histórico. Nessa lista, temos uma lista com os parametros de busca 
                                              #seguida de uma lista com X para plotagem, seguida de uma outra lista com o Y para plotagem. E esse padrão segue até o fim do histórico
        for w in range(len(lista_pronta)):
            if lista_pronta[w] == parametros:#veremos se há o parametro que está sendo dados está no histórico do usuario
                if parametros[0] == '3':#caso haja, veremos se está se tratando da busca 3
                    for r in range(len(lista_pronta[w+2])):
                        y.append(float(lista_pronta[w+2][r]))
                    plotmodule.plot_3(lista_pronta[w+1], y, parametros[1])#se for o caso, preparamos o conteúdo do histórico para plotagem, e chamamos a função resposável para tal 
                    return 1
                elif parametros[0] == '4':
                    for r in range(len(lista_pronta[w+1])):
                        x.append(float(lista_pronta[w+1][r]))
                    plotmodule.plot_4(x, lista_pronta[w+2], parametros[1])
                    return 1
                elif parametros[0] == '5':#se estiver se tratando de uma busca 5, preparemos o conteúdo e chamaremos a função para plotagem
                    for t in range(len(lista_pronta[w+2])):
                        y.append(float(lista_pronta[w+2][t]))
                    plotmodule.plot_5(lista_pronta[w+1], y, parametros[3])
                    return 1
                elif parametros[0] == '6':
                    listas = []
                    n = int(parametros[3])+2
                    label = lista_pronta[w+2:w+n+1]
                    separa = []
                    for r in range(len(lista_pronta[w+2:w+n])):
                        for f in range(len(lista_pronta[w+2:w+n][r])):
                            separa.append(int(lista_pronta[w+2:w+n][r][f]))
                        y.append(separa)
                        separa = []
                    for t in range(len(lista_pronta[w+1])):
                        x.append(int(lista_pronta[w+1][t]))
                    plotmodule.plot_6(x, y, label[-1], lista_pronta[w][3])
                    return 1
                elif parametros[0] == '7':
                    for r in range(len(lista_pronta[w+2])):
                        y.append(float(lista_pronta[w+2][r]))
                    plotmodule.plot_7(lista_pronta[w+1], y, parametros[1])
                    return 1
                elif parametros[0] == '8':
                    listas = []
                    n = 4
                    separa = []
                    for r in range(len(lista_pronta[w+2:w+n])):
                        for f in range(len(lista_pronta[w+2:w+n][r])):
                            separa.append(float(lista_pronta[w+2:w+n][r][f]))
                        y.append(separa)
                        separa = []
                    for t in range(len(lista_pronta[w+1])):
                        x.append(int(lista_pronta[w+1][t]))
                    plotmodule.plot_8(x, y, parametros[1])
                    return 1
                elif parametros[0] == '12':
                    for r in range(len(lista_pronta[w+2])):
                        y.append(int(lista_pronta[w+2][r]))
                    plotmodule.plot_12(lista_pronta[w+1], y, parametros[1])
                    return 1

def escrever_persistir(numero, parametros, resultado):#função que auxilia a persistência de buscas realizadas
    persistir = arquivos.retorna_user()
    arquivo = open("{}.txt".format(persistir), "a")#abrimos o arquivo o qual o usuário está logado
    armazenar = numero+','+parametros+' '+resultado+'\n'
    arquivo.write(armazenar)#e nele escrevemos o numero da busca, os parametros dela, e o resultado para ela
    arquivo.close()
    
def organiza_resultado(x, y, numero):#função que auxilia a persistência de buscas realizadas
    nova_string1 = ""
    nova_string2 = ""
    
    for k in range(len(x)):
        nova_string1 += str(x[k])+','#o resultado de x já processado convertido em uma string
        
    if numero == '6':
        for i in range(len(y)):
            for j in range(len(y[i])):
                nova_string2 += str(y[i][j])+','
            nova_string2 = nova_string2[0:len(nova_string2)-1]
            nova_string2 += ' '
        nova_string1 = nova_string1[0:len(nova_string1)-1]
        nova_string2 = nova_string2[0:len(nova_string2)-1]
        retorno = nova_string1+' '+nova_string2
        return retorno
    
    elif numero != '6' and numero != '8':
        for i in range(len(y)):
            nova_string2 += str(y[i])+','#o resultado de y já processado convertido em uma string
        nova_string1 = nova_string1[0:len(nova_string1)-1]#tiremos uma vírgula final desnecessária
        nova_string2 = nova_string2[0:len(nova_string2)-1]
        retorno = nova_string1+' '+nova_string2#aqui retornaremos o resultado pronto para ser escrito
        return retorno
    
    else:
        for i in range(len(y)):
            for k in range(len(y[i])):
                nova_string2 += str(y[i][k])+','
            nova_string2 = nova_string2[0:len(nova_string2)-1]+' '
        nova_string1 = nova_string1[0:len(nova_string1)-1]
        retorno = nova_string1+' '+nova_string2
        return retorno
