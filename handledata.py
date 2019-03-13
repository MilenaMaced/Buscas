arq = open("vgsales.csv",  'r')
big_data = [line.strip().split(',') for line in arq]
big_data.remove(big_data[0])
arq.close()

def intervalo_anos():#função que gera um intervalo de anos
    while True:
        print("Digite 0 para sair da busca")#o usuário tem a opção de sair da busca logo quando entrar
        try:
            ano1 = int(input("Digite o ano inicial\n"))
            if ano1 == 0:#se digitar 0, o intervalo não será criado
                return 1
            else:
                try:
                    ano2 = int(input("Digite o ano final\n"))#se digitar qualquer outra coisa, iremos ao segundo ano do intervalo
                    if ano2 == 0:
                        return 1
                    elif ano1 < 1980 or ano1 > 2020 or ano2 > 2020 or ano2 < 1980 or ano1 == ano2:#e então, verificaremos se os anos dados fazem parte dos anos que estão na base de dados
                        print("As informações dadas são inválidas.")
                    else:
                        return ano1, ano2
                except ValueError:
                    print("Valor inválido.")
        except ValueError:
                    print("Valor inválido.")

def publicadoras():
    publicadoras = []
    for k in range(len(big_data)):
        if big_data[k][5] not in publicadoras:
            publicadoras.append(big_data[k][5])
    return publicadoras

def generos(base, genre):#função para simples conferência dos gêneros disponíveis
    lista_generos = []
    ordem = 1
    
    for i in range(len(base)):#criação da lista
        if base[i][4] not in lista_generos:#quando um genero que não está na lista é achado, ele é colocado na mesma
            lista_generos.append(base[i][4])
            
    if genre not in lista_generos:#se o genero que estiver sendo passado não estiver na lista
        while True:
            opt = input("Digite 1 para acessar a lista de gêneros\nDigite 2 para sair\n")#o usuário tem a opção de checar a lista com os generos disponíveis, ou se quiser, pode sair
            if opt == '1':   #caso ele selecione 1, a lista com os generos será dada
                lista_generos = sorted(lista_generos)
                retorno = ""
                for k in range(len(lista_generos)):
                    retorno += ("{} {}\n".format(ordem, lista_generos[k]))
                    ordem += 1

                print(retorno)
                return 1
            elif opt == '2':#caso ele selecione 2, ele sairá dessa função automática
                return 1
            else:
                print("Comando inválido.")#caso digite algo alem das opções, as opções serão apresentadas novamente
    return 0
