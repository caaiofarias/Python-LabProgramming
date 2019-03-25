def pasto(i,j,T):
    global ovelha_pasto
    global lobo_pasto
    global linha
    global coluna
    if T[i][j] == '.':
        T[i][j] = 'x'
    elif T[i][j] == '#':
        return    
    elif T[i][j] == 'x':
        return
    elif T[i][j] == 'k':
        ovelha_pasto += 1
        T[i][j] = 'x'
    elif T[i][j] == 'v':
        lobo_pasto += 1
        T[i][j] = 'x'
    if i-1 >= 0:
        pasto(i-1,j,T)
    if j+1 < coluna:
        pasto(i,j+1,T)
    if i+1 < linha:
        pasto(i+1,j,T)
    if j-1 >= 0:
        pasto(i,j-1,T)
    
def matriz(l,c,caract):
    matr = []
    ovelha = 0
    lobo = 0
    for i in range(l):
        lista = []
        for j in range(c):
            if caract[i][j] == 'k':
                ovelha += 1
            if caract[i][j] == 'v':
                lobo += 1
            lista.append(caract[i][j])
        matr.append(lista)
    return matr, lobo, ovelha
busca = 1
lincol = input().split(" ")
caracteres = []

for d in range(int(lincol[0])):
    dados = input()
    caracteres.append(dados)

linha = int(lincol[0])
coluna = int(lincol[1])

p,lobo_inicial,ovelha_inicial= matriz(linha,coluna,caracteres)

for i in range(linha):
    for j in range(coluna):
        if p[i][j] == "k" or p[i][j] == "v":#só entra na recursão se for diferente de uma cerca ou já visitado
            busca = 1
            ovelha_pasto = 0
            lobo_pasto = 0
            pasto(i,j,p)
            if lobo_pasto >= ovelha_pasto:
                ovelha_inicial -= ovelha_pasto
            else:
                lobo_inicial -= lobo_pasto
            
print("%d %d" %(ovelha_inicial,lobo_inicial))
    
