casos = int(input())
m = []

for i in range(casos):
    nConj = int(input())
    for linha in range(nConj):
        x = [int(x) for x in input().split()]
        del x[0]
        conj = set(x)#usando set para criar os conjuntos
        m.append(conj)
    nOp = int(input())
    for j in range(nOp):
        oper = [int(x) for x in input().split()]
        if oper[0] == 1:#Intersecção
            print(len(m[oper[1]-1].intersection(m[oper[2]-1])))#retorna a qtd de elementos na operção solicita
        elif oper[0] == 2:#Uniao
            print(len(m[oper[1]-1].union(m[oper[2]-1])))#retorna a qtd de elementos na operção solicita
    m = []
    
            
            
        
        
            
