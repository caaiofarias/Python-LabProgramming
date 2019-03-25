#URI 2139
dia25 = 360
listaDias = [31,29,31,30,31,30,31,31,30,31,30,31]

while True:
    try:
        casos= [int(x) for x in input().split()]
        if casos[0] != 1:
            if sum(listaDias[0:casos[0]-1]) + casos[1] > dia25:
                print("Ja passou!")
            elif sum(listaDias[0:casos[0]-1]) + casos[1] == dia25:
                print("E natal!")
            elif sum(listaDias[0:casos[0]-1]) + casos[1] == dia25 - 1:
                print("E vespera de natal!")
            else:
                print("Faltam %d dias para o natal!"%(dia25 - (sum(listaDias[0:casos[0]-1]) + casos[1])))
        else:
            print("Faltam %d dias para o natal!"%(dia25 - casos[1]))
    except:
        break
#URI 2140
while True:
    casos = int(input())
    if casos == 0:
        break
    
    for i in range(casos):
        pessoas = int(input())
        if pessoas %2 == 0:
            print((pessoas - 2)*2 + 2)
        else:
            print((pessoas - 1)*2 +1)
        
