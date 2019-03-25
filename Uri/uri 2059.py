entrada = [int(x) for x in input().split()]

p = entrada[0]
j1 = entrada[1]
j2 = entrada[2]
r = entrada[3]
a = entrada[4]

if p == 1 and r == 0 and a == 0:
    if (j1 + j2) % 2 == 0:
        print("Jogador 1 ganha!")
    else:
        print("Jogador 2 ganha!")
elif p == 1 and r == 1 and a == 0:
    print("Jogador 1 ganha!")
elif p == 1 and r == 0 and a == 1:
    print("Jogador 1 ganha!")
elif p == 1 and r == 1 and a == 1:
    print("Jogador 2 ganha!")
if p == 0 and r == 0 and a == 0:
    if (j1 + j2) % 2 == 0:
        print("Jogador 2 ganha!")
    else:
        print("Jogador 1 ganha!")
elif p == 0 and r == 1 and a == 0:
    print("Jogador 1 ganha!")
elif p == 0 and r == 1 and a == 1:
    print("Jogador 2 ganha!")
elif p == 0 and r == 0 and a == 1:
    print("Jogador 1 ganha!")


