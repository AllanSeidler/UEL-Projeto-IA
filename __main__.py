import deck

if __name__=='__main__':
    d = deck.Deck(1)
    with open('log','w',newline='',encoding='utf-8-sig') as f:
        for c in d.cards:
            print(c['id'],end='\n',file=f)
