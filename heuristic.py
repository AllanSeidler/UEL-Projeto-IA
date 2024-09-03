'''
As funções de heuristica devem seguir o seguinte modelo:
    
    def decision(v:int, d:Deck) -> bool:
        ...
        return True/False

    Onde v é o valor da mão e d um deck contendo cartas.
'''
from deck import Deck
import statistics

'''Um dealer que puxa cartas até ter 17 ou mais pontos na mão.'''
def dealer_verdadeiro(v:int, d:Deck) -> bool:
    return v<17

'''Se tem chance de perder, desiste.'''
def medrosa(v:int, d:Deck) -> bool:
    i = 9
    c = d.counter[i]
    while c==0:
        i-=1
        c = d.counter[i]
    return (v+i)<22

'''Se tem chance de aumentar o valor da mão, puxa uma carta.''' 
def corajosa(v:int, d:Deck) -> bool:
    i = 0
    c = d.counter[i]
    while c==0:
        i+=1
        c = d.counter[i]
    return (v+i)<22

'''É um meio termo entre a corajosa e o dealer verdadeiro'''
def dealer_falso(v:int, d:Deck) -> bool:
    if v>17:
        i = 0
        c = d.counter[i]
        while c==0:
            i+=1
            c = d.counter[i]
        return ((v+i)<22)
    else:
        return False

'''Vê a carta do topo do baralho.'''
def trapaceiro(v:int, d:Deck) -> bool:
    return (d.cards[0]+v)<22

'''Faz estimativa por media.'''
def media(v:int, d:Deck) -> bool:
    soma = 0
    for i in range(10):
        soma+=i*d.counter[i]
    return (v+soma/d.size) <= 21

'''Faz estimativa por mediana.'''
def mediana(v:int, d:Deck) -> bool:
    return (v+statistics.median(d.cards)) <= 21

'''Faz estimativa por moda.'''
def moda(v:int, d:Deck) -> bool:
    c = 0
    for i in range(10):
        if d.counter[i] > d.counter[c]:
            c=i
    return (c+1+v)<22    

