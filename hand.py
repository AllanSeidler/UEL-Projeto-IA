'''
Uma mão de cartas
'''
from deck import Deck

class Hand:
    def __init__(self):
        self.cards=[]
        self.value=0
    
    def clear(self):
        self.cards.clear();

    def draw_card(self,deck: Deck):
        card = deck.draw()
        if(card['value']==11):
            if(self.value>10):
                card['value']=1
        self.value+=card['value']
    
    
