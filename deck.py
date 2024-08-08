'''
Cria um deck de tamanho n*52 cartas
'''
import random as rdm

class Deck:

    def __init__(self, n):
        self.cards =[]
        
        suits=['♦','♠','♥','♣']
        for i in range(n):
            for s in suits:
                self.cards.append({'id':'A'+s,'value':11})
                for v in range(2,11):
                    self.cards.append({'id':str(v)+s,'value':v})
                for f in ['J','Q','K']:
                    self.cards.append({'id':f+s,'value':10})
        rdm.shuffle(self.cards)

    def draw(self):
        return self.cards.pop()
