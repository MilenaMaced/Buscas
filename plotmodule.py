import matplotlib.pyplot as plt
from matplotlib import style
style.use("bmh")
global cores
cores = ["#300742", "#36164e", "#3b2457", "#423663", "#4b4c75", "#566b8a", "#61849d", "#6a9cae", "#73b4bf", "#7cc9cf", "#6fccb3", "#6fcc9d", "#6fcc92"]

def plot_3(x, y, regiao):
    fig = plt.figure()
    axl = plt.subplot2grid((1,1),(0,0))
    axl.set_facecolor('white')
    for label in axl.xaxis.get_ticklabels():
        label.set_rotation(45)

    plt.scatter(x, y, color = ["#300742", "#36164e", "#3b2457", "#423663", "#4b4c75", "#566b8a", "#61849d", "#6a9cae", "#73b4bf", "#7cc9cf"])
    plt.xlabel('Plataforma')
    plt.ylabel('Média')
    plt.title('Média X Plataforma, Região {}'.format(regiao))
    plt.subplots_adjust(left =0.10,bottom = 0.16, right = 0.94, top = 0.85)
    plt.show()
    
def plot_4(x, y, genero):
    fig = plt.figure()
    axl = plt.subplot2grid((1,1),(0,0))
    axl.grid(False)
    axl.set_facecolor('white')
    plt.pie(x, labels = y, shadow = True, startangle = -180, explode = (0.1, 0, 0, 0, 0), autopct = '%1.1f%%', colors = ["#4b4c75", "#566b8a", "#61849d", "#6a9cae", "#73b4bf",])
    plt.title('Locais X Média, Gênero {}'.format(genero))
    plt.show()

def plot_5(x, y, genero):
    fig = plt.figure()
    axl = plt.subplot2grid((1,1),(0,0))
    axl.set_facecolor('white')
    X = []
    for k in range(len(x)):
        X.append(str(x[k]))
    for label in axl.xaxis.get_ticklabels():
        label.set_rotation(45)
    plt.plot(X, y, color = '#4b4c75')
    plt.xlabel('Anos')
    plt.ylabel('Média')
    plt.title('Média Vendas Globais X Ano, {}'.format(genero))
    plt.subplots_adjust(left =0.10, bottom = 0.16, right = 0.94, top = 0.85)
    plt.show()
    
def plot_6(x, final, genres, X):
    fig = plt.figure()
    axl = plt.subplot2grid((1,1),(0,0))
    axl.set_facecolor('white')
    X_axl = []
    for k in range(len(x)):
        X_axl.append(str(x[k]))
        
    for label in axl.xaxis.get_ticklabels():
        label.set_rotation(45)
        
    for d in range(len(final)):
        plt.plot(X_axl, final[d], label = "{}".format(genres[d]))
        plt.xlabel('Anos')
        plt.ylabel('Quantidade de Jogos')
        plt.title('Quantidade de Jogos X {} Maiores Gêneros'.format(X))
    plt.subplots_adjust(left =0.10,bottom = 0.16, right = 0.94, top = 0.85) 
    plt.legend()
    plt.show()

def plot_7(x, y, publicadora):
    fig = plt.figure()
    axl = plt.subplot2grid((1,1),(0,0))
    axl.grid(False)
    axl.set_facecolor('white')
    for label in axl.xaxis.get_ticklabels():
        label.set_rotation(45)
    axl.bar(x, y, color = cores)
    plt.xlabel("Plataformas")
    plt.ylabel("Vendas Globais")
    plt.title("Vendas Globais de cada Plataforma, Publicadora {}\n".format(publicadora))
    plt.subplots_adjust(left =0.1,bottom = 0.16, right = 0.94, top = 0.80)
    plt.show()

def plot_8(x, y, topX):
    fig = plt.figure()
    axl = plt.subplot2grid((1,1),(0,0))
    axl.set_facecolor('white')
    plt.plot(x, y[0], color = "#423663", label = "NA")
    plt.plot(x, y[1], color = "#61849d", label = "EU")
    plt.xlabel("Ranking")
    plt.ylabel("Vendas de Jogos")
    plt.title("\nTop {} de Jogos de Vendas em NA e EU ".format(topX))
    plt.subplots_adjust(left =0.10,bottom = 0.16, right = 0.94, top = 0.85)
    plt.legend()
    plt.show()
    
def plot_12(x, y, genero):
    fig = plt.figure()
    axl = plt.subplot2grid((1,1),(0,0))
    axl.set_facecolor('white')
    plt.scatter( x,y,color ="#6fccb3")
    plt.xlabel("Plataformas")
    plt.ylabel("Quantidades de Jogos")
    plt.title("\n10 plataformas com mais jogos do gênero {}\n".format(genero))
    plt.subplots_adjust(left =0.10,bottom = 0.16, right = 0.94, top = 0.85)
    plt.show()
 
