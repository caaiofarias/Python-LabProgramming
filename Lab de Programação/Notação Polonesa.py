from math import floor,ceil
listaAr = ['*','/','+','-']
pilha = []
final = []
entrada = ""
while True:
    try:
        entrada = input()
        exp = entrada.split()
        exp.reverse()
        for i in exp:
            if i in listaAr:
                if len(pilha) == 0:
                    continue
                else:
                    operando1 = pilha.pop(-1)
                    if len(pilha) == 0:
                        continue
                    else:
                        operando2 = pilha.pop(-1)
                        if i == "*":
                            res = operando1*operando2
                            pilha.append(res)
                        elif i == "/":
                            res = operando1/operando2
                            temp = str(res)
                            temp2 = temp[0]
                            if temp[0].isdigit() == False:
                                temp2 = temp[1]
                            if int(temp2) - res >= 0.555:
                                pilha.append(ceil(res))
                            else:
                                pilha.append(floor(res))
                        elif i == "+":
                            res = operando1+operando2
                            pilha.append(res)
                        elif i == "-":
                            res = operando1-operando2
                            pilha.append(res)
                        
            else:
                pilha.append(int(i))
            
        if len(pilha) == 1:
            final.append(pilha[0])
            pilha = []
    except (EOFError):
        break
#imprimindo lista
for i in final:
    print(i)
