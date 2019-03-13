import processamento
import plotmodule
import arquivos

while True:
    arquivos.usuarios()
    arquivo = open("usuarios.txt", "r")
    dados = []
    for k in arquivo:
        dados.append(k.split("\n"))
    arquivo.close()
    if len(dados) == 0:
        arquivos.adm()
    verifica = arquivos.ler_arquivo()
    if verifica == 0:
        comando = input("O usuário não está cadastro no sistema\nDigite 1 para tentar novamente\nDigte 2 para acessar o guia de instrução\nDigite 3 para finalizar o programa\n")
        if comando == '1':
            False
        elif comando == '2':
            print(" Bem vindo ao guia de instrução\n",
                  "Se você está usando o sistema pela primeira vez, você poderá logar usando o login padrão e senha padrão do sistema.\n",
                  "Ao logar na conta padrão, selecione a opção 8 para criar uma nova conta com o cargo de gerente.\n",
                  "Aconselhamos que ao fazer o cadastro da nova conta, saia da conta padrão, faça login na nova conta criada, e exclua a conta padrão.\n"
                  " Apenas o gerente é capaz de criar uma nova conta, ou apagar uma conta existe.\n")
            False
        elif comando == '3':
            False
            break


