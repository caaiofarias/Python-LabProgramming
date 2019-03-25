while True:
    try:
        ent = [int(x) for x in input().split()]
        dist = (ent[2] - ent[0])*(ent[2] - ent[0]) + (ent[3]-ent[1])*(ent[3]-ent[1])#calculo de distancia entre fiddle e o inimigo
        dist = dist ** 0.5 # raiz da dist
        t = ent[4]*1.5#velocidade
        dist+= t
        if ent[5] + ent[6] >=dist:#compara o raio com a distancia, se se for maior ou igual acertou
            print("Y")
        else:
            print("N")
    except:
        break
