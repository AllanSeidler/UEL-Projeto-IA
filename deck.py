'''
Cria um deck de tamanho n*52 cartas
'''
import random as rdm

class Deck:
    def __init__(self):
        self.cards = []
        self.size = 0
    
    '''Retira a carta no topo do deck e a retorna.'''
    def draw(self) -> int:
        card = self.cards.pop(0)
        self.counter[(card-1)%10]-=1
        self.size -= 1
        return card

    
    def reset(self,n):
        self.size= n*52
        self.cards.clear()

        self.counter = [4*n]*9
        self.counter.append(16*n)

        self.cards.extend([11]*self.counter[0])
        for i in range(1,10):
            self.cards.extend([i+1]*self.counter[i])

        rdm.shuffle(self.cards)