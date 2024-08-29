from deck import Deck
from heuristic import *

'''
    O Player deve trabalhar com uma heuristica para
    tomada de decição e um deck para puxar as cartas.
'''
class Player:
    def __init__(self, heuristic, deck: Deck):
        self.is_stand = False
        self.heuristic = heuristic    
        self.hand_value = 0
        self.deck = deck
    
    
    '''Puxa as primeiras duas cartas.'''
    def start(self):
        self.draw_card()
        self.draw_card()



    '''Define o valor da mão puxando cartas do deck até que uma ação de stand seja feita.'''
    def set_hand(self) -> int: # dar um nome melhor
        while self.is_stand == False:
            if(self.heuristic(self.hand.value)):
                self.draw_card(self,self.deck)
            else:
                self.is_stand=True
        
        return self.get_hand_value()
    

    '''Puxa uma carta do deck e já verifica e processa os 'ás'.'''
    def draw_card(self,deck: Deck):
        card = deck.draw()
        if(card==11):
            if(self.value>10):
                card=1
        self.value+=card
    
    
    '''Retorna o valor da mão. 0 se maior que 21.'''
    def get_hand_value(self) -> int:
        if self.hand_value > 21: 
            return 0
        else: 
            return self.hand_value

    
    '''Limpa a mão removendo todas as cartas.'''
    def clear_hand(self):
        self.value=0



'''É um tipo especifico de player.'''
class Dealer(Player):
    def __init__(self, deck: Deck):
        super().__init__(true_dealer,deck) # a heuristica é sempre true_dealer
        self.secret_card = 0
        

    '''Mantem uma das cartas iniciais em segredo.'''
    def start(self):
        self.draw_card
        self.secret_card = self.deck.draw()
    

    '''Soma o valor da carta secreta e procede normalmente.'''
    def set_hand(self) -> int:
        self.value+=self.secret_card
        return super().set_hand()


    

