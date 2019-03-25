lCaju,cCaju,liM,colM = [int(x) for x in input().split()]
matriz = []
dp = []
maior = 0
for i in range(lCaju):#criando a matriz de cajus
    linha = []
    temp = input().split()
    for j in range(cCaju):
        linha.append(int(temp[j]))
    matriz.append(linha)
for i in range(lCaju):#criando matriz para Programação dinamica
    linha = []
    for j in range(cCaju):
        linha.append(0)
    dp.append(linha)
for i in range(lCaju):
    dp[i][0] = 0#atribuindo 0 no primeiro elemento das linhas da matriz
    for j in range(colM):
        dp[i][0] += matriz[i][j]#atribuindo o valor correspondente na matriz de caju
    for j in range(1,cCaju-colM+1):#range da coluna de caju - coluna pedida + 1, pois começo em 1, tirando a primeira col
        dp[i][j] = dp[i][j-1] + matriz[i][j+colM-1] - matriz[i][j-1]#basicamente cria uma copia independente para dp
for j in range(cCaju-colM+1):#após ter 2 matriz "identicas", somo as linhas e colunas indo para a coluna primeiro, e depois as linhas
    matriz[0][j] = 0#inicio com 0 a posição que será somada
    for i in range(liM):
        matriz[0][j] += dp[i][j]#somo o valor correspondente a ela na outra matriz(a DP)
    for i in range(1,lCaju-liM+1):#desço uma linha e somo a proxima coluna a ela, guardando na posição i
        matriz[i][j] = matriz[i-1][j] + dp[i+liM-1][j] - dp[i-1][j]
        if matriz[i][j] > maior:#guardo o maior valor 
            maior = matriz[i][j]
print(maior)   
        
