from random import randint
from colections import Counter

def geracao_inicial():
    """retorna uma lista de 100 pais para a geração 0, cada um sendo uma string 
    de 24 bits em que cada posição das rainhas nas linhas é codificada por 3 bits"""
    bitString = ""
    for i in range(0, 24): 
        x = str(random.randint(0, 1))
        bitString += x
    return [bitString for x in range(100)]

def recombinacao(): """aqui precisa achar uma parte pra dividir e cruzar, achei um link que mostra varias 
                maneiras de fazer: https://www.obitko.com/tutorials/genetic-algorithms/portuguese/crossover-mutation.php"""
    filhos []
    for x in range(100):
        for y in range(100):
            if(x != y):