from random import randint
from random import shuffle
import random
import itertools
import string

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
    for k in range(0, 24, 3):
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


#seleção de pais OK
def pais(list):
    paislist = []
    ftnspais = []
    
    pais = []
    torneio = []
    
    
    #selecionando 5 pais aleatoriamente
    paislist = random.sample(list, 5)
    ftnspais = fitness(paislist)

    #encontro os dois maiores da lista e defino os pais

    pais.append(paislist[ftnspais.index(max(ftnspais))])
    ftnspais[ftnspais.index(max(ftnspais))] = 0

    #repito pro segundo pai
    pais.append(paislist[ftnspais.index(max(ftnspais))])
    return(pais)

#recombinação OK
def recombinacao(list):
    filhos = []
    xpoint = random.randrange(3, 24, 3)
    pai = list[0]
    mae = list[1]
    filhos.append(pai[:xpoint] + mae[xpoint:])
    filhos.append(mae[:xpoint] + pai[xpoint:])
    
    return(filhos)

#mutação OK
def mutacao(list):
    mutado = [] 
    separador = ""
    escSeparado = []
    escolhido = random.choice(list)
    print (escolhido)
    for n in range(0, 24, 3):
        escSeparado.append(escolhido[n:n+3])

    xnumber1 = random.randrange(0, 7)
    xnumber2 = random.randrange(0, 7)
    if(xnumber1 == xnumber2 & xnumber2 == 7):
        xnumber2 = xnumber2-1
        rainhaTemp = escSeparado[xnumber1]
        escSeparado[xnumber1] = escSeparado[xnumber2]
        escSeparado[xnumber2] = rainhaTemp
    elif((xnumber1 == xnumber2 & xnumber2 == 0) | xnumber1 == xnumber2):
        xnumber2 = xnumber2+1
        rainhaTemp = escSeparado[xnumber1]
        escSeparado[xnumber1] = escSeparado[xnumber2]
        escSeparado[xnumber2] = rainhaTemp
    else:
        rainhaTemp = escSeparado[xnumber1]
        escSeparado[xnumber1] = escSeparado[xnumber2]
        escSeparado[xnumber2] = rainhaTemp

        
    mutado = separador.join(escSeparado)
    
    return mutado
 
    
def sobreviventes(list):
    ftnspop = fitness(list)
         

geracao = geracao_zero(10)
print (geracao)
print (fitness(geracao))
pais = (pais(geracao))
print (fitness(pais))
print (pais)
print (recombinacao(pais))
print (mutacao(geracao))
