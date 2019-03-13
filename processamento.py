import datapersistence
import sys
import handledata

arq = open("vgsales.csv",  'r')
big_data = [line.strip().split(',') for line in arq]
big_data.remove(big_data[0])
arq.close()
sys.setrecursionlimit(10000)

def busca_3(regiao):
    plataformas  = []
    media = []
    x = []
    y = []
    numero_busca = "3"
    soma_vendas = 0
    divisor = 0
    media_plataforma = 0

    #varrendo a lista com todas as informações, para então poder criar o novas listas com apenas o que for necessário para a busca 3
    if regiao == 'NA':
        n = 6
    elif regiao == 'EU':
        n = 7
    elif regiao == 'JP':
        n = 8
    elif regiao == 'Global':
        n = 9
    elif regiao == 'Other':
        n = 10
            
    for i in range(len(big_data)):
        if big_data[i][2] not in plataformas:
            plataformas.append(big_data[i][2])
    for p in range(len(plataformas)):#varre a lista com todas as plataformas
        for k in range(len(big_data)):#varre a lista criada com o parâmetro fornecido pelo usuário
            if big_data[k][2] == plataformas[p]:#verifica se a plataforma da lista principal é igual a plataforma da lista de plataformas
                soma_vendas += float(big_data[k][n])#soma o numero de vendas
                divisor += 1#calcula  a quantidade de divisores
        media_plataforma = soma_vendas/divisor
        media.append(media_plataforma)
        soma_vendas = 0
        divisor = 0
        media_plataforma = 0
        
    #criação do top 10
    for top in range(10):
        maior_media = media[0]
        plataforma_maior = plataformas[0]
        for f in range (len(media)):
            if media[f] >= maior_media:
                maior_media = media[f]
                for k in range (len(plataformas)):
                    if f == k:
                        plataforma_maior = plataformas[k]
                
        x.append(plataforma_maior)
        y.append(maior_media)
        media.remove(maior_media)
        plataformas.remove(plataforma_maior)
        
    resultado = datapersistence.organiza_resultado(x, y, numero_busca)#o resultado da busca será organizado para que possa ser armazenado no histórico
    datapersistence.escrever_persistir(numero_busca, regiao, resultado)#assim que organizado, escrevemos no histórico
    retorno = (x, y, regiao)
    return retorno#a função retorna os valores x, y e região, para serem plotados em uma nova função
 
def chamada_3():#chamada para auxiliar a busca 3
    while True:
        print("Em qual região deseja saber o top 10 da média de vendas por plataforma?")
        regiao = input(" Digite 0 para sair\n Digite 1 para NA Sales\n Digite 2 para EU Sales\n Digite 3 para JP Sales\n Digite 4 para Global Sales\n Digite 5 para Other Sales\n")
        if regiao != '1' and regiao != '2' and regiao != '3' and regiao != '4' and regiao != '5' and regiao != '0':
            print("Comando inválido.")
        elif regiao == '0':
            False
            break
        else:
            if regiao == '1':
                regiao = "NA"
            elif regiao == '2':
                regiao = "EU"
            elif regiao == '3':
                regiao = "JP"
            elif regiao == '4':
                regiao = "Global"
            elif regiao == '5':
                regiao = "Other"
            parametros = ["3", regiao]#nossos parametros serão o numero da busca, e a regiao
            checa = datapersistence.ler_persistir(parametros)#aqui verificaremos se há esses parametros no históricos
            if checa != 1:#se caso houver, a função ler_persistir retornará 1, e não processará uma nova busca
                return busca_3(regiao)

def busca_4(genero):
    lista_generos = []
    b4_1 = []
    b4_2 = []
    b4_3 = []
    b4_4 = []
    ordem = 1
    vendas_index = 6
    numero_busca = "4"
    
    b4_1 = big_data[0:5000]
    b4_2 = big_data[5001:10000]
    b4_3 = big_data[10001:15000]
    b4_4 = big_data[15001:len(big_data)]
    def conta_genero(lista, genero):
        if len(lista) == 0:
            return len(lista)
        else:
            if lista[0][4] == genero:
                return 1 + (conta_genero(lista[1:len(lista)], genero))
            else:
                return conta_genero(lista[1:len(lista)], genero)
            
    def calculo_vendas(lista, indice, jogos, genero):
        vendas = 0
        media = 0
        x = []
        while indice <= 10:
            for k in range(len(lista)):
                if lista[k][4] == genero:
                    vendas += float(lista[k][indice])
            media = vendas/jogos
            x.append(media)
            indice += 1
            vendas = 0
            media = 0
        return x
    
    jogos = conta_genero(b4_1, genero)+conta_genero(b4_2, genero)+conta_genero(b4_3, genero)+conta_genero(b4_4, genero)
    armazenar = calculo_vendas(big_data, vendas_index, jogos, genero)
    x = []
    for k in range (len(armazenar)):
        novo = 100 * armazenar[k]
        x.append(novo)
    y = ["NA", "EU", "JP", "Other", "Global"]

    resultado = datapersistence.organiza_resultado(x, y, numero_busca)
    datapersistence.escrever_persistir(numero_busca, genero, resultado)
    retorno = (x, y, genero)
    return retorno


def chamada_4():
    while True:
        genero = input("Digite 0 para sair da busca\nDigite um gênero para realizar a busca\n")
        if len(genero)>  0:
            a = genero[0].upper()
            genero = a+genero[1:]
        if genero == '0':
            False
            break
        else:
            verifica = handledata.generos(big_data, genero)
            if verifica == 0:
                parametros = ["4", genero]
                checa = datapersistence.ler_persistir(parametros)
                if checa != 1:
                    return busca_4(genero)
            
def busca_5 (anoInicial, anoFinal, genero):
    ano1 = anoInicial
    ano_reserva = anoInicial
    ano2 = anoFinal
    anos = []
    lista_anos = []
    dicio_genero = []
    auxiliar = 0
    x = []
    y = []
    continua1 = True
    verifica = True
    
    if(anoInicial > anoFinal):#verificamos se o usuário colocou o ano inicial como sendo maior que o final
        anoInicial = ano2
        anoFinal = ano1#se caso isso acontecer, não há problema! Ajustamos para que o maior seja o final, e o menor seja o inicial
       
    while anoInicial <= anoFinal:#criaremos uma lista de dicionarios
        comp_5 = [anoInicial, auxiliar]
        n = []
        dicio_genre = {'ano': anoInicial, 'generos': n}#o dicionario terá uma chave para o seu ano, e para cada ano, haverá um dicionário
        anos.append(comp_5)
        dicio_genero.append(dicio_genre)
        lista_anos.append(anoInicial)
        anoInicial += 1
    
    for s in range(len(anos)):
        anoAuxiliar = anos[s][0]
        for i in range(len(big_data)):
            if big_data[i][3] != 'N/A' and int(big_data[i][3]) == anoAuxiliar:#filtramos a passagem por anos "vazios"
                for j in range(len(dicio_genero)):
                    if dicio_genero[j]['ano'] == anoAuxiliar and big_data[i][4] not in dicio_genero[j]['generos']:
                        dicio_genero[j]['generos'].append(big_data[i][4])#e colocamos os generos que há para aquele ano na chave de 'generos'
    def func_1 ():
        somaGlobal = 0
        cont = 0
        mediaGlobal = 0
                               
        for a in range(len(dicio_genero)):
            continua = True
            if genero not in dicio_genero[a]['generos']:
                continua = False
    
            if continua == True:
                for i in range(len(big_data)):
                    if big_data[i][3] != 'N/A':
                        if (int(big_data[i][3]) == dicio_genero[a]['ano']) and (big_data[i][4] == genero):
                            somaGlobal += float(big_data[i][10])
                            cont += 1
                mediaGlobal = somaGlobal/cont
                for k in range(len(anos)):
                    if anos[k][0] == dicio_genero[a]['ano']:
                        anos[k][1] = mediaGlobal
                somaGlobal = 0
                cont = 0
                mediaGlobal = 0
    func_1()
    for a in range (len(anos)):
        x.append(anos[a][0])
        y.append(anos[a][1])
    
    numero_busca = "5"
    resultado = datapersistence.organiza_resultado(x, y, numero_busca)#organiza os resultados de x e y para escrever no histórico
    parametros = str(ano_reserva)+','+str(anoFinal)+','+genero#prepara os parametros
    datapersistence.escrever_persistir(numero_busca, parametros, resultado)#e então escreve
    retorno = (x, y, genero)#auxilio para o retorno do necessário para plotagem
    return retorno


def chamada_5():#chamada para auxiliar a busca 5
    while True:
        anos = handledata.intervalo_anos()
        if anos == 1:
            False
            break
        elif anos != None:
            genero = input("Digite um genero\n")
            if len(genero) > 0:
                a = genero[0].upper()
                genero = a+genero[1:]
            verifica = handledata.generos(big_data, genero)
            if verifica == 0:
                parametros = ["5", str(anos[0]), str(anos[1]), genero]
                checa = datapersistence.ler_persistir(parametros)
                if checa != 1:
                    return busca_5(anos[0], anos[1], genero)

def busca_6(anoInicial, anoFinal, X):
    lista_genero = []
    y = []
    x = []
    linhas = []
    ano1 = anoInicial
    ano2 = anoFinal
    ano_reserva = anoInicial
    continua = True
    genres = []
    somas = []
    completa = []
    separar = []
    
    if(anoInicial > anoFinal):#organiza o maior e o menor para caso o usuário digite o maior primeiro
        anoInicial = ano2
        anoFinal = ano1
              
    while anoInicial <= anoFinal:
        n = []
        dicio_genero = {'ano': anoInicial, 'generos': n, 'vendas': []}#criação de um dicionario para auxiliar na organização
        lista_genero.append(dicio_genero)#todos os dicionarios serão colocados nesta lista
        x.append(anoInicial)#todos os anos do intervalo ficarão aqui
        completa.append(separar)#criação de uma lista que terá elementos como listas
        separar = []
        anoInicial += 1

    for s in range(len(lista_genero)):#varremos a lista de dicionarios
        anoAuxiliar = lista_genero[s]['ano']#pegamos o ano do dicionario
        for i in range(len(big_data)):#varremos a nossa base
            if big_data[i][3] != 'N/A' and int(big_data[i][3]) == anoAuxiliar:#e verificamos se o ano da base naquela posição é igual ao ano do nosso dicionario
                if big_data[i][4] not in lista_genero[s]['generos']:#se for, veremos se o genero daquele ano está na lista de generos da chave do dicionario
                    lista_genero[s]['generos'].append(big_data[i][4])#se não estiver, colocaremos este gênero lá
                    lista_genero[s]['vendas'].append(0)#e colocamos um valor que servirá para contar a quantidade de jogos daquele gênero
    
    for k in range(len(lista_genero)):
        anoAuxiliar = lista_genero[k]['ano']
        for j in range(len(big_data)):
            if big_data[j][3] != 'N/A' and int(big_data[j][3]) == anoAuxiliar:
                for h in range(len(lista_genero[k]['generos'])):
                    if lista_genero[k]['generos'][h] == big_data[j][4]:#aqui verificamos se o genero daquele ano é igual ao genero da nossa base
                        for u in range(len(lista_genero[k]['vendas'])):
                            if u == h:
                                lista_genero[k]['vendas'][u] += 1#se for, uma unidade será colocada em 'vendas', que representa o quantitativo dos jogos

    if continua == True:
        for k in range(len(lista_genero)):#aqui iremos criar uma lista de gêneros baseada nos gêneros presentes no intervalo
            for i in range(len(lista_genero[k]['generos'])):
                if lista_genero[k]['generos'][i] not in genres:
                    genres.append(lista_genero[k]['generos'][i])
        soma = 0
        for p in range(len(genres)):
            for b in range(len(lista_genero)):
                for c in range(len(lista_genero[b]['generos'])):
                    if lista_genero[b]['generos'][c] == genres[p]:
                        soma += lista_genero[b]['vendas'][c]#somamos os jogos por gêneros e colocamos numa lista
            somas.append(soma)
            soma = 0
        #criação do top X
        if len(somas) - X > 0: #se somas -  X for igual a zero, significa que o numero de generos na base é igual ao top
            for n in range(len(somas)- X):
                menor = somas[0]
                menor_genre = genres[0]
                for f in range(len(somas)):
                    if somas[f] < menor:
                        menor = somas[f]
                        for y in range(len(genres)):
                            if y == f:
                                menor_genre = genres[y]
                genres.remove(menor_genre)
                somas.remove(menor)
                
        nova_somas = []
        nova_genres = []
        axl_org = genres
        for s in range(len(axl_org)):#organização do maior ao menor
            maior_soma = somas[0]
            maior_genre = genres[0]
            for o in range(len(somas)):
                if somas[o] > maior_soma:
                    maior_soma = somas[o]
                    maior_genre = genres[o]
            nova_somas.append(maior_soma)
            nova_genres.append(maior_genre)
            somas.remove(maior_soma)
            genres.remove(maior_genre)
    
        somas = nova_somas
        genres = nova_genres
        #aqui iremos verificar se há algum ano que não possui algum gênero da nossa lista de gêneros, porque se houver, esse gênero somará 0
        for t in range(len(genres)):
            for q in range(len(lista_genero)):
                for r in range(len(lista_genero[q]['generos'])):
                    if lista_genero[q]['generos'][r] == genres[t]:
                        completa[q].append(lista_genero[q]['vendas'][r])
                if genres[t] not in lista_genero[q]['generos']:
                    completa[q].append(0)
        organiza = []
        final = []
        for l in range(len(completa[0])):
            for v in range(len(completa)):
                organiza.append(completa[v][l])
            final.append(organiza)
            organiza = []
        numero_busca = "6"
        nova_string = ""
        resultado = datapersistence.organiza_resultado(x, final, numero_busca)
        
        for m in range(len(genres)):
            nova_string += str(genres[m])+','
        nova_string = nova_string[0:len(nova_string)-1]
        resultado = resultado+' '+nova_string
        parametros = str(ano_reserva)+','+str(anoFinal)+','+str(X)
        datapersistence.escrever_persistir(numero_busca, parametros, resultado)
        retorno = (x, final, genres, X)
        return retorno
    

def chamada_6():
    while True:
        anos = handledata.intervalo_anos()
        if anos == 1:
            False
            break
        elif anos != None:
            if anos != 1:
                try:
                    genero = int(input("Digite a quantidade de gêneros\n"))
                    if genero > 0 and genero < 13:
                        parametros = ["6", str(anos[0]), str(anos[1]), str(genero)]
                        checa = datapersistence.ler_persistir(parametros)
                        if checa != 1:
                            return busca_6(anos[0], anos[1], genero)
                    else:
                        print("Quantidade de gêneros não permitida.\n")
                except ValueError:
                    print("Valor inválido.")
                

def busca_7(publicadora):
    dados = {}
    vendasGlobais = 0
    x = []
    y = []
    
    for i in range(len(big_data)):
        if(publicadora == big_data[i][5]):
            dados[big_data[i][2]] = 0
    for plataformas in dados:
        vendasGlobais = 0
        for k in range(len(big_data)):
            if(plataformas == big_data[k][2] and publicadora == big_data[k][5]):
                vendasGlobais += float(big_data[k][10]) 
            dados[plataformas] = vendasGlobais 
  
    for plataformas in dados:
        x.append(plataformas)
        y.append(dados[plataformas])
    
    numero_busca = "7"
    resultado = datapersistence.organiza_resultado(x, y, numero_busca)
    datapersistence.escrever_persistir(numero_busca, publicadora, resultado)
    retorno = (x, y, publicadora)
    return retorno
  
def chamada_7():    
    while True:
        publicadora = input("Digite 0 para sair da busca\nDigite uma publicadora para realizar a busca:\n")
        if publicadora == '0':
            False
            break
        lista_publicadoras = handledata.publicadoras()
        if publicadora not in lista_publicadoras:
            listar = input("Publicadora não encontrada.\nDigite 1 para acessar a lista de publicadoras.\nDigite 2 para tentar novamente\n")
            if listar == '1':
                lista_publicadoras = sorted(lista_publicadoras)
                for k in range(len(lista_publicadoras)):
                    print(lista_publicadoras[k])
            elif listar == '2':
                False

            else:
                print("Comando inválido.")
        else:
            parametros = ["7", publicadora]
            checa = datapersistence.ler_persistir(parametros)
            if checa != 1:
                return busca_7(publicadora)


def busca_8(topX):
    listaNa=[]
    listaEu= []
    lista = []
    maiorNa = 0
    maiorEu = 0
    listaNa_Y1 = []
    listaEu_Y2 = []
    x = []
    y = []
    
    for i in range(len(big_data)):
        listaNa.append(float(big_data[i][6]))
        listaEu.append(float(big_data[i][7]))
    maiorNa = listaNa[0]
    maiorEu = listaEu[0]
    
    for n in range(topX):
        for j in range(len(listaNa)):
            if listaNa[j]>maiorNa:
                maiorNa = listaNa[j]
        for k in range(len(listaEu)):
            if listaEu[k]>maiorEu:
                maiorEu = listaEu[k]        
        tupla = (maiorNa,maiorEu)
        lista.append(tupla)
        listaNa.remove(maiorNa)
        listaEu.remove(maiorEu)
        maiorNa = listaNa[0]
        maiorEu = listaEu[0]
    
 
    for a in range(len(lista)):
            listaNa_Y1.append(lista[a][0])
            listaEu_Y2.append(lista[a][1])
            x.append(a+1)
            
    y.append(listaNa_Y1)
    y.append(listaEu_Y2)
    numero_busca = "8"
    nova_string = ""
    resultado = datapersistence.organiza_resultado(x, y, numero_busca)
    datapersistence.escrever_persistir(numero_busca, str(topX), resultado)
    retorno = (x, y, topX)
    return retorno
    
def chamada_8():
    topX = 1
    while topX !=0:
        print("\nDigite 0 para sair da busca")
        try:
            topX = int(input("Digite um Top X para jogos mais vendidos: "))
            if(topX!=0):
                if(topX>0 and topX<15000):
                    parametros = ["8", str(topX)]
                    checa = datapersistence.ler_persistir(parametros)
                    if checa != 1:
                        return busca_8(topX)
                else:
                    print("Valor inválido.")
        except ValueError:
                    print("Valor inválido.")
        
def busca_12(genero):
    dicionario = {}
    novoDicionario  = {}
    maior=0
    p=""
    x = []
    y = []
    
    for i in range(len(big_data)):
        dicionario[big_data[i][2]] = 0 #preencher o dicionario com chaves com nome da plataforma e colocar zero no valor da chave 
        
    for plataformas in dicionario: #percorrer o dicionario 
        cont = 0
        for k in range(len(big_data)):
            if(genero == big_data[k][4] and plataformas == big_data[k][2]): #Verificar o genero, se é igual o que o usuario digitou, e verificar se as plataformas sao iguais
                cont += 1                   #quando a condição for verdadeira, o contador soma 1
            dicionario[plataformas] = cont  #de acordo que contador vai adicionando, ele vai modificando o valor do dicionario com base naquela chave
    
    for i in range(10): #pegar top 10
        maior = 0
        p = ""
        for plataformas in dicionario:
            if(dicionario[plataformas]>maior):  #verificar maior elemento
                maior = dicionario[plataformas]
                p = plataformas
        novoDicionario[p] = maior #Armazeno a maior quantidade de jogos  daquele genero e a plataforma que será a chave
        del(dicionario[p])      #Deletar dado do dicionario antigo apos encontra maior  quantidade de jogos  daquele genero
    for plataformas in novoDicionario:
        x.append(plataformas)
        y.append(novoDicionario[plataformas])
        
    numero_busca = "12"
    resultado = datapersistence.organiza_resultado(x, y, numero_busca)
    datapersistence.escrever_persistir(numero_busca, genero, resultado)
    retorno = (x, y, genero)
    return retorno
   
def chamada_12():
    while True:
        genero = input("Digite 0 para sair da busca\nDigite um gênero para realizar a busca\n")
        if len(genero)>  0:
            a = genero[0].upper()
            genero = a+genero[1:]
        if genero == '0':
            False
            break
        else:
            verifica = handledata.generos(big_data, genero)
            if verifica == 0:
                parametros = ["12", genero]
                checa = datapersistence.ler_persistir(parametros)
                if checa != 1:
                    return busca_12(genero)
