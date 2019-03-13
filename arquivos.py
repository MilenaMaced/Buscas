import os
import user

def usuarios():#criação de um arquivo que será necessário no sistema de login
    arquivo = open("usuarios.txt", "a")
    arquivo.close()
    
def adm():
    arquivo = open("admin.txt", "w")
    armazenar = "Administrador,gerente,admin,admin\n"
    arquivo.write(armazenar)
    arquivo.close()
    arq = open("usuarios.txt", "w")
    armazenar = "admin\n"
    arq.write(armazenar)


def criar_arquivo():
    while True:
        nome_usuario = input("Digite 0 para sair\nDigite o nome do usuário: ")
        if len(nome_usuario) > 0 and ' ' not in nome_usuario and '\\n' not in nome_usuario:
            if nome_usuario == '0':
                False
                break
            cargo = input("Cargo na empresa: ")
            continua = True
            
            if cargo == 'gerente' or cargo == 'funcionario':
                login = input("Digite o login: ")
                if len(login) > 0 and ' ' not in login  and '\\n' not in login:
                    senha = input("Digite a senha: ")
                    if len(senha)> 0 and ' ' not in senha  and '\\n' not in senha:
                        arq_usuarios = open("usuarios.txt", "r")#abrimos o arquivo com todos os usarios
                        
                        checar_dados = []
                        novo_checar = []
                        for r in arq_usuarios:
                            checar_dados.append(r)
                        for t in range(len(checar_dados)):
                            novo_checar.append(checar_dados[t].strip())
                        arq_usuarios.close()
                        if len(novo_checar) != 0:
                            for k in range(len(novo_checar)):
                                if novo_checar[k] == login:#e checamos se há algum um usuário com esse login
                                    print("Login já pertence a outro usuário\n")
                                    continua = False
                        
                        if continua == True:
                            arquivo = open("{}.txt".format(login), "w")#se não houver, podemos criar a conta
                            armazenar = nome_usuario+','+cargo+','+login+','+senha+'\n'
                            arquivo.write(armazenar)
                            arquivo.close()
                            arq_usuarios = open("usuarios.txt", "a")
                            arq_usuarios.write(login+'\n')
                            arq_usuarios.close()
                            print("Usuário cadastrado com sucesso.")
                            False
                            break
                    else:
                        print("Senha não pode estar vazia ou conter espaço.")
                else:
                    print("Login não pode estar vazio ou conter espaço.")
            else:
                print("Os cargos disponíveis são 'funcionario' ou 'gerente'. Tente um deles.")
        else:
            print("Login não pode estar vazio ou conter espaço.")

def ler_arquivo():#função para efetuar login
    while True:
        print("\n")
        print("==============================================================================\n")
        print("                                                                    PORTAL INICIAL\n")
        print("==============================================================================\n")
        arq = open("usuarios.txt", "r")
        dados_arq = []
        for i in arq:
            dados_arq.append(i.strip())
        arq.close()
        if len(dados_arq) == 1 and dados_arq[0] == 'admin':
            print("             Login padrão: admin         Senha padrão: admin                  \n")
        login = input("Login: ")
        senha = input("Senha: ")
        checar =  open("usuarios.txt", "r")
        checar_dados = []
        novo_checar = []
        for r in checar:
            checar_dados.append(r)
        for t in range(len(checar_dados)):
            novo_checar.append(checar_dados[t].strip())
        checar.close()
        global persistir
        if len(novo_checar) != 0:
            for t in range(len(novo_checar)):
                if novo_checar[t] == login:#verificamos se o login passado está no arquivo com todos os logins
                    arquivo = open("{}.txt".format(login), "r")#se estiver, podemos abrir o arquivo do usuario
                    lista = []
                    dados = []
                    for h in arquivo:
                        recebe = h.split('\n')
                        del(recebe[len(recebe)-1])
                        #print(recebe)
                        dados.append(recebe)
                    arquivo.close()
                    #print(dados)
                    for k in range(len(dados)):
                        for i in range(len(dados[k])):
                            novos = dados[k][i].strip().split(',')
                            lista.append(novos)
                    #print(lista)
                    if lista[0][3] != senha:#e verifica se a senha dada está correta
                        print("Senha incorreta. Por favor tente novamente.")
                        return 1
                    elif lista[0][3] == senha:#se estiver, verificamos se o usuario tem acesso ao menu de gerente ou de funcionari
                        if lista[0][1] == 'gerente':
                            persistir = login
                            user.gerente()
                            return 1
                        elif lista[0][1] == 'funcionario': 
                            persistir = login
                            user.funcionario()
                            return 1
        return 0
def retorna_user():
    return persistir
    
def exclui():
    while True:
        arq = open("usuarios.txt", "r")
        dados = []
        for r in arq:
            dados.append(r.strip())
        arq.close()
        arquivo = input("Digite 0 para sair.\nDigite o login da conta que deseja remover: ")
        if arquivo == '0':
            return
        if arquivo in dados:
            dados.remove(arquivo)
            arq = open("usuarios.txt", "w")
            for k in range(len(dados)):
                arq.write(dados[k]+'\n')
            arq.close()
            os.remove("{}.txt".format(arquivo))
            print("Usuário removido com sucesso.")
            False
            if persistir == arquivo:
                print("Programa finalizado.")
                return 1
        else:
            print("O usuário não foi encontrado")
            comando = input("\nDigite 0 para sair.\nDigite 1 para tentar novamente.\n")
            if comando == '0':
                return
