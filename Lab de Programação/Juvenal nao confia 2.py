def criaMatriz(li,col):
    global matriz
    for i in range(li):
        linha = []
        temp = input()
        for j in range(col):
            linha.append(temp[j])
        matriz.append(linha)

def contaNavios(i,j,matriz):
    global temp
    global linhaM
    global colunaM
    global cont
    if matriz[i][j] == "#":
        if j-1>=0:
            if matriz[i][j-1] == "#":
                contaNavios(i,j-1,matriz)
        if j+1 < colunaM:
            if matriz[i][j+1]=="#":
                contaNavios(i,j+1,matriz)
        if i-1 >=0:
            if matriz[i-1][j] == "#":
                contaNavios(i-1,j,matriz)
        if i+1 < linhaM:
            if matriz[i+1][j] == "#":
                contaNavios(i+1,j,matriz)
            matriz[i][j] = cont
    elif matriz[i][j] == ".":
        return
    elif matriz[i][j] == int():
        return
cont = 0
temp = []
matriz = []
resp = []
entrada = [int(x) for x in input().split()]
linhaM = entrada[0]
colunaM = entrada[1]
criaMatriz(entrada[0],entrada[1])#chamando função para criar a matriz do campo de batalha
for i in range(linhaM):
    for j in range(colunaM):
        if matriz[i][j] == "#":
            contaNavios(i,j,matriz)#função recursiva para contar os navios
            cont+=1
print(matriz)
for i in range(linhaM):
    for j in range(colunaM):
        if matriz[i][j] != str and matriz[i][j] not in temp and matriz[i][j] != ".":#colocando os navios numa lista temporaria
            temp.append(matriz[i][j])
disparos = int(input())
for i in range(disparos):#efetuando os disparos
    tiro = [int(x) for x in input().split()]
    matriz[tiro[0]-1][tiro[1]-1] = "D"
for u in range(linhaM):#vendo os navios que sobrou e colocando em outra lista
    for v in range(colunaM):
        if type(matriz[u][v]) == int and matriz[u][v] not in resp:
            resp.append(matriz[u][v])

print(len(temp) - len(resp)) #imprime os navios nao destruidos com os destruidos
