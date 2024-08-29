'''
As funções de heuristica devem seguir o seguinte modelo:
    
    def decision(v:int, d:Deck) -> bool:
        ...
        return True/False

    Onde v é o valor da mão e d um deck contendo cartas.
'''
from deck import Deck


'''Um dealer que puxa cartas até ter 17 ou mais pontos na mão.'''
def true_dealer(v:int, d:Deck) -> bool:
    return v<17


