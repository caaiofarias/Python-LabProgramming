def criaMatriz(li,col):
    global matriz
    for i in range(li):
        linha = []
        temp = input()
        for j in range(col):
            linha.append(temp[j])

        matriz.append(linha)
def contaNavios(i,j):
    global matriz
    global cont
    global colunaM
    global linhaM
    global listaNavios
    if matriz[i][j] == ".":
        return
    if matriz[i][j] == int():
        return
    if matriz[i][j] == "#":
        if i-1>=0:
            matriz[i][j] = cont
            contaNavios(i-1,j)
        if j + 1 < colunaM:
            matriz[i][j] = cont
            contaNavios(i,j+1)
        if i+1 < linhaM:
            matriz[i][j] = cont
            contaNavios(i+1,j)
        if j-1>=0:
            matriz[i][j] = cont
            contaNavios(i,j-1)
        listaNavios[cont] += 1
resp = 0      
listaNavios = []
matriz = []
cont = 0
linhaM,colunaM = [int(x) for x in input().split()]
criaMatriz(linhaM,colunaM)
for i in range(linhaM):
    for j in range(colunaM):
        if matriz[i][j] == "#":
            listaNavios.append(cont)
            contaNavios(i,j)
            listaNavios[cont] -=cont
            cont+=1

disparos = int(input())
for i in range(disparos):
    tiro = [int(x) for x in input().split()]
    if matriz[tiro[0]-1][tiro[1]-1] != ".":
        listaNavios[matriz[tiro[0]-1][tiro[1]-1]] -=1
resp += listaNavios.count(0)
print(resp)
