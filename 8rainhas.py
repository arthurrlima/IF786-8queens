from random import randint
from random import shuffle
import random
import itertools

#func geracao_zero OK
def geracao_zero(qtd):
    separador = ""
    bitMap = ['000', '001', '010','011', '100','101','110','111']
    bitList = []
    
    
    for n in range(qtd):
        random.shuffle(bitMap)
        x = itertools.permutations(bitMap)
        strBit = separador.join(next(x))
        bitList.append(strBit)
    
    return(bitList)    
        

def checkcolisao(string):
    colisao = 0
    rainhas = []
    
    #preenchendo lista com as posições das rainhas OK
    for k in range(0, 21, 3):
        rainha = int(string[k:k+3], 2)
        rainhas.append(rainha)

    #percorrendo rainhas
    #não ta funcioando
    for idx in range(0, 8):
        for chk in range(idx+1,8):
            if rainhas[idx] == rainhas[chk]+chk:
                colisao += 1
            elif rainhas[idx] == rainhas[chk]-chk
                colisao += 1

    return(colisao)       

def fitness(list):
    
    for n in range(len(list)):
        stringbit = list[n]
        ftns = 1/(1+checkcolisao(stringbit))

    return(ftns)

print (fitness(geracao_zero(10)))

#def recombinacao():
