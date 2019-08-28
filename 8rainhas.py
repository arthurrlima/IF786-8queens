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
    ftnspaisord = []
    pais = []
    
    #selecionando 5 pais aleatoriamente
    paislist = random.sample(list, 5)
    ftnspais = fitness(paislist)
    
    #ordenando o fitness dos 5 pais selecionados e depois selecionando os dois melhores
    ftnspaisord = sorted(ftnspais)
    mlrsfntspais = fntspaisord[:2]

    #vai varrer o array de melhores fitness e o de fitness calculado inicialmente para saber de qual pai é aquele fitness
    for n in range(len(ftnspais)):
        for m in range(len(mlrsfntspais)):
            if ftnspais[n] = mlrsfntspais[m]:
                pais[m] = paislist[n]
    
    return(pais)
    #print (pais(geracao_zero(10)))

#def recombinacao(pais):
