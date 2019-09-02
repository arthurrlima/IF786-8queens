import random
def converterd_b(n):
    binario = ""
    while(True):
        binario = binario + str(n%2)
        n = n//2
        if n == 0:
            break
    binario = binario[::-1]
    binario = int(binario)
    return binario

def converterb_d(n):
    decimal = 0
    n = str(n)
    n = n[::-1]
    tam = len(n)
    for i in range(tam):
        if n[i] == "1":
            decimal = decimal + 2**i
    return decimal

def geracao_zero(qtd):
    numeros = []
    binarios = []
    for n in range(qtd):
        numeros.append(random.randint(0,32))
    for k in range(qtd):
        binarios.append(converterd_b(numeros[k]))
    binarios = binarios.sort()

    return binarios

def fitness(list):
    fitness = []
    decimal = []
    for n in range(len(list)):
        decimal.append(converterb_d(list[n]))
    for k in range(len(list)):
        fitness.append(decimal[k] * decimal[k])
    
    return fitness

def pais(list):
    pais = []
    ftnspais = []
    ftnspais = fitness(list)

    pais.append(list[ftnspais.index(max(ftnspais))])
    pais.append(list[ftnspais.index(max(ftnspais))-1])

    return pais




geracao = geracao_zero(4)
print (geracao)
print (pais(fitness(geracao)))