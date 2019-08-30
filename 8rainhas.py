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
        
#recebe string de bits, cria lista de int, retorna n colisoes
def checkcolisao(string):
    colisao = 0
    rainhas = []
    
    #preenchendo lista com as posições das rainhas
    for k in range(0, 21, 3):
        rainha = int(string[k:k+3], 2)
        rainhas.append(rainha)

    #percorrendo rainhas
    #calculo de colisoes OK 
    for idx in range(len(rainhas)):
        aux = 0

        for chk in range(idx,len(rainhas)):
          
            if rainhas[chk] == rainhas[idx]+aux and idx != chk:
                colisao += 1

            elif rainhas[chk] == rainhas[idx]-aux and idx != chk:
                colisao += 1

            aux +=1

    return(colisao)      
    
#recebe lista de string, passa string pro calculo de colisão, retorna lista dos fitness da população
#calculo de fitness OK
def fitness(list):
    ftnslist = []
    
    for n in range(len(list)):
        stringbit = list[n]
        ftns = 1/(1+checkcolisao(stringbit))
        ftnslist.append(ftns)

    return(ftnslist)

def pais(list):
    paislist = []
    ftnspais = []
    
    pais = []
    torneio = []
    
    
    #selecionando 5 pais aleatoriamente
    paislist = random.sample(list, 5)
    ftnspais = fitness(paislist)

    #encontro o maior da lista, passo pro pais e removo da lista
    pais.insert(0, paislist[ftnspais.index(max(ftnspais))])
    paislist[ftnspais.index(max(ftnspais))] = 0

    #repito pro segundo pai
    pais.insert(1, paislist[ftnspais.index(max(ftnspais))])
    
    return(pais)


def recombinacao(list):
    filhos = []
    xpoint = random.randrange(3, 24, 3)
    pai = list[0]
    mae = list[1]
    filhos.insert(0, pai[:xpoint] + mae[xpoint:])
    filhos.insert(1, mae[:xpoint] + pai[xpoint:])

    #for n in range(len(list)):
     #   if n == 0:
      #      filhos[n][:nmrrand] = (list[n][:nmrrand])
       #     filhos[n][nmrrand:].append(list[n+1][nmrrand:])
        #else:
         #   filhos[n][:nmrrand].append(list[n][:nmrrand])
          #  filhos[n][nmrrand:].append(list[n-1][nmrrand:])

    
    return(filhos)

pais = pais(geracao_zero(10))
print (pais)
print (recombinacao(pais))
