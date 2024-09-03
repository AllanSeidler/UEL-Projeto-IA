from deck import Deck
from heuristic import *
from ia import Player
from ia import Dealer
from random import seed
import matplotlib.pyplot as plt
import numpy as np


seed(4)
NUMERO_DE_DECKS = 6
TOTAL_DE_RODADAS = 10000


heuristics = [medrosa, corajosa, media, mediana, moda, dealer_falso, trapaceiro]


def rodada(player:Player,dealer:Dealer):

    player.start()
    dealer.start()
    ph = player.set_hand() # player hand
    dh = dealer.set_hand() # dealer hand
    
    # print(f'player: {player.hand_value}, dealer: {dealer.hand_value}')
    dealer.clear_hand()
    player.clear_hand()

    if(ph>dh): # player vence
        return 1
    elif(dh>ph): # dealer vence
        return -1
    else: # empate
        return 0
    


if __name__=='__main__':
    resultados = [0]*(TOTAL_DE_RODADAS+1)
    deck = Deck()

    dealer = Dealer(deck)
    player = Player(None,deck)
    
    
    with open('log','w',newline='',encoding='utf-8-sig') as f:
        for h in heuristics: # passa por todas as heuristicas
            player.heuristic=h # define a heuristica atual
            
            for i in range(1,TOTAL_DE_RODADAS+1):
                if(deck.size<52):
                    deck.reset(NUMERO_DE_DECKS)
                r = rodada(player,dealer)
                resultados[i] = resultados[i-1] + r # vetor com a pontuacao corrente usando a heuristica atual

    