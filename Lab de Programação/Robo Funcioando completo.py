def repos(caracI,inst):
    if inst == "D":
        if caracI == "L":
            caracI="S"
        elif caracI == "O":
            caracI = "N"
        elif caracI == "N":
            caracI = "L"
        elif caracI == "S":
            caracI = "O"
    elif inst == "E":
        if caracI == "L":
            caracI = "N"
        elif caracI == "O":
            caracI = "S"
        elif caracI == "N":
            caracI = "O"
        elif caracI == "S":
            caracI = "L"
    return caracI
while True:
    figurinha = 0
    posI = [0,0]
    matriz = []
    coord = ["N","S","L","O"]
    linha = ""
    cont = 0
    caracI = ""
    achou = False
    casos = [int(x) for x in input().split()]
    if casos == [0,0,0]:
        break
    for i in range(casos[0]):
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
    while achou == False:
        for i in range(casos[0]):
            for j in range(casos[1]):
                if matriz[i][j] == caracI:
                    achou = True
                    posI = [i,j]
            if achou == True:
                break
    testes = input()
    for instruct in range(len(testes)):
        if testes[instruct] == "D":
            caracI = repos(caracI,"D")
            matriz[posI[0]][posI[1]] = caracI
        elif testes[instruct] == "E":
            caracI = repos(caracI,"E")
            matriz[posI[0]][posI[1]] = caracI
        elif testes[instruct] == "F":
            if caracI == "N":
                if posI[0]-1 < 0:
                    posI=posI
                else:

                    try:
                        x = matriz[posI[0]-1][posI[1]] # tenta ver qual oq tem na pos a frente do robo
                        if x == ".":
                            matriz[posI[0]][posI[1]] = "."#a posição q o robo tava vira ponto
                            posI = posI[0]-1,posI[1]# a nova posicao do robo é a pos inicial
                            matriz[posI[0]][posI[1]] = caracI#a posicao onde esta o robo vira o carac do robo
                        elif x == "*":
                            figurinha+=1
                            matriz[posI[0]][posI[1]] = "."
                            posI = posI[0]-1,posI[1]
                            matriz[posI[0]][posI[1]] = caracI
                        elif x == "#":
                            posI = posI
                    except:
                        posI = posI
            elif caracI == "S":
                try:
                    x = matriz[posI[0]+1][posI[1]]
                    if x == ".":
                        matriz[posI[0]][posI[1]] = "."#a posição q o robo tava vira ponto
                        posI = posI[0]+1,posI[1]
                        matriz[posI[0]][posI[1]] = caracI
                    elif x == "*":
                        figurinha += 1
                        matriz[posI[0]][posI[1]] = "."
                        posI = posI[0]+1,posI[1]
                        matriz[posI[0]][posI[1]] = caracI
                    elif x == "#":
                        posI = posI
                except:
                    posI = posI
            elif caracI == "L":
                try:
                    x = matriz[posI[0]][posI[1]+1]
                    if x == ".":
                        matriz[posI[0]][posI[1]] = "."#a posição q o robo tava vira ponto
                        posI = posI[0],posI[1]+1
                        matriz[posI[0]][posI[1]] = caracI
                    elif x == "*":
                        figurinha += 1
                        matriz[posI[0]][posI[1]] = "."#a posição q o robo tava vira ponto
                        posI = posI[0],posI[1]+1
                        matriz[posI[0]][posI[1]] = caracI
                    elif x == "#":
                        posI = posI
                except:
                    posI = posI
            elif caracI == "O":
                if posI[1]-1 < 0:
                    posI = posI
                else:
                    
                    try:
                        x = matriz[posI[0]][posI[1]-1] # tenta ver qual oq tem na pos a frente do robo
                        if x == ".":
                            matriz[posI[0]][posI[1]] = "."#a posição q o robo tava vira ponto
                            posI = posI[0],posI[1]-1# a nova posicao do robo é a pos inicial
                            matriz[posI[0]][posI[1]] = caracI#a posicao onde esta o robo vira o carac do robo
                        elif x == "*":
                            figurinha+=1
                            matriz[posI[0]][posI[1]] = "."
                            posI = posI[0],posI[1]-1
                            matriz[posI[0]][posI[1]] = caracI                
                        elif x == "#":
                            posI = posI

                    except:
                        posI = posI
    print(figurinha)     
    
