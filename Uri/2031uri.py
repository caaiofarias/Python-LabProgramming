casos = int(input())+1
for i in range(casos-1):
    ent = input()
    ent2 = input()
    if ent == "ataque" and ent2 == "pedra":
        print("Jogador 1 venceu")
    elif ent2 == "ataque" and ent == "pedra":
        print("Jogador 2 venceu")
    elif ent == "pedra" and ent2 == "papel":
        print("Jogador 1 venceu")
    elif ent2 == "pedra" and ent == "papel":
        print("Jogador 2 venceu")
    elif ent == "ataque" and ent2 == "papel":
        print("Jogador 1 venceu")
    elif ent2 == "ataque" and ent == "papel":
        print("Jogador 2 venceu")
    elif ent == "papel" and ent2 == "papel":
        print("Ambos venceram")
      
    elif ent == "pedra" and ent2 == "pedra":
        print("Sem ganhador")

    elif ent == "ataque" and ent2 == "ataque":
        print("Aniquilacao mutua")
