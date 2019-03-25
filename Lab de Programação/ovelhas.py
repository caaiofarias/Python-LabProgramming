def campo(i,j,matriz):#cria e separa cada campo, retornando o numero de ovelhas e lobos
    global linhaM
    global colunaC
    global loboCampo
    global ovelhaCampo
    if matriz[i][j] == "k":
        ovelhaCampo +=1
        matriz[i][j] = "x"
    elif matriz[i][j] == "v":
        loboCampo += 1
        matriz[i][j] = "x"
    elif matriz[i][j] == ".":
        matriz[i][j] = "x"
    elif matriz[i][j] == "#":
        return
    elif matriz[i][j] == "x":
        return
    #Chamada recursiva para caminhar na matriz    
    if i - 1 >=0:
        campo(i-1,j,matriz)
    if i+1 < linhaM:
        campo(i+1,j,matriz)
    if j-1 >=0:
        campo(i,j-1,matriz)
    if j+1 < colunaM:
        campo(i,j+1,matriz)
matriz = []
cont = 0
linha = ""
lobo = 0
ovelha = 0
entrada = [int(x) for x in input().split()]
linhaM = entrada[0]
colunaM = entrada[1]
#criando a matriz e identificando o numero total de ovelhas e lobos inicialmente      
for i in range(entrada[0]):
    linha += input()
    linha += "Q"
while cont != len(linha):
    l = []#linha de cada matriz
    for elem in linha:
        if elem == "k":
            ovelha += 1
        elif elem == "v":
            lobo += 1
        if elem != "Q":
            l.append(elem)#acrescentando os elementos na linha
            cont+=1
        else:
            matriz.append(l)#colocando a linha na matriz
            l=[]#iniciando a linha vazia novamente
            cont+=1
print(matriz)
#percorre a matriz chamando a função campo para contar em cada campo qual o nª de ovelhas e lobos, e fazendo a operação descrita no problema
for i in range(linhaM):
    for j in range(colunaM):
        ovelhaCampo = 0
        loboCampo = 0
        campo(i,j,matriz)
        if loboCampo >= ovelhaCampo:#se o n de lobos naquele campo for maior que o de ovelha, tira as ovelhas
            ovelha -= ovelhaCampo
        else:#se for o de ovelhas maior que os dos lobos, tira os lobos
            lobo -= loboCampo
print("%d %d"%(ovelha,lobo))
