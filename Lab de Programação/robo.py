def reposicionaI(caracI,inst,posF):
    temp = posF
    if caracI == "N" and inst == "D":
        caracI = "L"
        try:
            posF = [posF[0]+1,posF[1]+1]
        except:
            posF = temp
    elif caracI == "N" and inst == "E":
        caracI = "O"
        try:
            posF = [posF[0]+1,posF[1]-1]
        except:
            posF = temp
    elif caracI == "S" and inst == "D":
        caracI = "L"
        try:
            posF = [posF[0]-1,posF[1]+1]
        except:
            posF = temp
    elif caracI == "S" and inst == "E":
        caracI == "O"
        try:
            posF = [posF[0]-1,posF[1]-1]
        except:
            posF = temp
    elif caracI == "O" and inst == "D":
        caracI = "N"
        try:
            posF = [posF[0]-1,posF[1]+1]
        except:
            posF = temp
    elif caracI == "O" and inst == "E":
        caracI = "S"
        try:
            posF = [posF[0]+1,posF[1]+1]
        except:
            posF = temp
    elif caracI == "L" and inst == "D":
        caracI = "S"
        try:
            posF = [posF[0]+1,posF[1]-1]
        except:
            posF = temp
    else:
        caracI = "N"
        try:
            posF = [posF[0]-1,posF[1]-1]
        except:
            posF = temp
    return caracI,posF
            
def repos(caracI,posI):
    global posF
    if caracI == "N":#aponta para a LINHA acima 
        try:
            matriz[posI[0]-1][posI[1]]
            posF = [posI[0]-1,posI[1]]
            print(posF)
        except:
            posF = posF
    elif caracI == "O":#aponta para a COLUNA A ESQUERDA
        try:
            matriz[posI[0]][posI[1]-1]
            posF = [posI[0],posI[1]-1]
        except:
            posF = posF
    elif caracI == "S":#aponta para a LINHA abaixo
        try:
            matriz[posI[0]+1][posI[1]]
            posF = [posI[0]+1,posI[1]]
        except:
            posF = posF
    else:#aponta para a COLUNA a direita
        try:
            matriz[posI[0]][posI[1]+1]
            posF = [posI[0],posI[1]+1]
        except:
            posF=posF
    return posF

resp = []
figurinha = 0
while True:
    resp.append(figurinha)
    coord = ['N','S','L','O']
    caracI = ""
    posI = [0,0]
    posF = [0,0]
    linha = ""
    cont = 0
    entrada1 = [int(x) for x in input().split()] #entrada valores
    if 0 in entrada1:# se for 0 quebra
        print(resp)
        break
    matriz = []
    for i in range(entrada1[0]):#lendo todas as linhas e colocando na str com o Q para separar as linhas
        linha += input()
        linha += "Q"
    while cont != len(linha):#colocando os valores dentro da matriz
        l = []
        for carac in linha:
            if carac in coord:
                caracI = carac
            if carac != "Q":
                l.append(carac)#colocando os carac em uma linha
                cont+=1
            else:
                matriz.append(l)#add a linha na matriz
                l = []
                cont+=1
    for i in range(entrada1[0]):#pegando a posição inicial do robô
        for j in range(entrada1[1]):
            if matriz[i][j] == caracI:
                posI = [i,j]#guardando a pos Inicial
                print(posI)
    print(matriz)
    #pegando para onde aponta o robo
    if caracI == "N":#aponta para a LINHA acima 
        try:
            matriz[posI[0]-1][posI[1]]
            posF = [posI[0]-1,posI[1]]
        except:
            posF = posI
    elif caracI == "O":#aponta para a COLUNA A ESQUERDA
        try:
            matriz[posI[0]][posI[1]-1]
            posF = [posI[0],posI[1]-1]
        except:
            posF = posI
    elif caracI == "S":#aponta para a LINHA abaixo
        try:
            matriz[posI[0]+1][posI[1]]
            posF = [posI[0]+1,posI[1]]
        except:
            posF = posI
    else:#aponta para a COLUNA a direita
        try:
            matriz[posI[0]][posI[1]+1]
        except:
            posF=posI
        
    temp = input()#instruções temp
    coach = []#colocando instruções em uma lista
    for i in temp:
        coach.append(i)
    for instruct in range(entrada1[2]):#fazendo as instruções
        if coach[instruct] == "D":
            l = reposicionaI(caracI,"D",posF)
            caracI = l[0]
            posF = l[1]
        elif coach[instruct] == "E":
            l = reposicionaI(caracI,"E",posF)
            caracI = l[0]
            posF=l[1]
        else:
            try:
                x = matriz[posF[0]][posF[1]]
            except:
                posF = posF
            if x == ".":
                posI = posF
                posF = repos(caracI,posI)
            elif x == "*":
                matriz[posF[0]][posF[1]] = "."
                figurinha+=1
                posI = posF
                posF = repos(caracI,posI)
            elif x == "#":
                posF = posF

