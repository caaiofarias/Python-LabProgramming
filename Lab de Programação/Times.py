def quicksort(v):
    if len(v) <= 1:
        return v
    less,equal,greater = [],[],[]
    pivot = v[0]
    for x in v:
        if x<pivot:
            less.append(x)
        elif x == pivot:
            equal.append(x)
        else:
            greater.append(x)
    return quicksort(less) + equal + quicksort(greater)
entrada = [int(x) for x in input().split()]

np = {}
cont = 0
dicTimes = {}
aux = 1
for nome in range(entrada[0]):#colocando todas as pessoas em um dicionario com a chave sendo a habilidade
    temp = input().split()
    np[int(temp[1])] = temp[0]
for i in range(1,entrada[1]+1):#criando um dicionario com o numero de times sendo as chaves(time1:[],time2:[]...)
    lista = []
    dicTimes[i] = lista
for i in range(entrada[0]):#iterando sobre todas as pessoas
    cont = 1#contador auxiliar para separar os times
    while True:
        if len(np) > 0:#caso o dicionario nao esteja vazio, ainda existem pessoas para serem alocadas em times
            pessoa = np.pop(max(np))#retira o maior e coloca no seu respectivo time(usando o contador como indice)
            dicTimes[cont].append(pessoa)
            cont+=1
        else:#caso nao, para
            break
        if cont > entrada[1]:#separando sempre as pessoas com a maior habilidade em times diferentes com esse contador
            break
matrizTimes = []#usando uma matriz para poder ordenar 
for i in dicTimes.values():
    matrizTimes.append(i)
for j in range(len(matrizTimes)):#ordenando com o quicksort os membros de cada equipe separada
    matrizTimes[j] = quicksort(matrizTimes[j])
for times in range(len(matrizTimes)):#imprimindo os times
    print("Time %d"%(times+1))
    for j in range(len(matrizTimes[times])):
        print(matrizTimes[times][j])
    print()

         
