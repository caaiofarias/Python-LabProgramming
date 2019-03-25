entrada = [int(x) for x in input().split()]

saida = entrada[0]
tempo = entrada[1]
fuso = entrada[2]

if sum(entrada) > 0:
    
    if saida + tempo + fuso < 24:
        print(sum(entrada))
    elif saida + tempo + fuso > 24:
        print(sum(entrada)- 24)
    
elif sum(entrada) < 0:
    print(sum(entrada) + 24)

else:
    print(0)
