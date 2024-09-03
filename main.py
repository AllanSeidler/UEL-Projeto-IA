from deck import Deck
from heuristic import *
from ia import Player
from ia import Dealer

NUMERO_DE_DECKS = 6


heuristics = [medrosa, corajosa, media, mediana, moda, dealer_falso, trapaceiro]

def rodada(player:Player,dealer:Dealer):
    player.start()
    dealer.start()
    ph = player.set_hand() # player hand
    dh = dealer.set_hand() # dealer hand
    
    # print(f'player: {player.hand_value}, dealer: {dealer.hand_value}')
    dealer.start()
    player.clear_hand()

    if(ph>dh): # player vence
        return 1
    elif(dh>ph): # dealer vence
        return -1
    else: # empate
        return 0
    



if __name__=='__main__':
    resultados = [0]*1000
    deck = Deck()

    dealer = Dealer(deck)
    player = Player(None,deck)

    with open('log','w',newline='',encoding='utf-8-sig') as f:
        for h in heuristics:
            player.heuristic=h
            somatoria=0

            for i in range(1000):
                if(deck.size<52):
                    deck.reset(NUMERO_DE_DECKS)
                resultados[i] = rodada(player,dealer)
                somatoria+=resultados[i]

            
            print(f'somatoria:{somatoria}, resultados:{resultados}',file=f)
