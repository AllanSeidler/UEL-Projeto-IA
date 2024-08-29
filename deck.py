'''
Cria um deck de tamanho n*52 cartas
'''
import random as rdm

class Deck:
    def __init__(self, n:int):
        self.cards = []
        self.counter = [4*n]*9
        self.counter.append(16*n)

        # suits=['♦','♠','♥','♣']
        for j in range(self.counter[0]):
            self.cards.append(11)
        for i in range(1,10):
            for j in range(self.counter[i]):
                self.cards.append(i+1)
        rdm.shuffle(self.cards)

    
    '''Retira a carta no topo do deck e a retorna.'''
    def draw(self) -> int:
        card = self.cards.pop()
        self.counter[card%11]-=1
        return card
