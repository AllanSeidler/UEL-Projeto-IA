import deck

if __name__=='__main__':
    # Gerando um deck de tamanho 6 (312 cartas)
    d = deck.Deck(6)

    # Imprimindo o deck no arquivo log
    with open('log','w',newline='',encoding='utf-8-sig') as f:
        for c in d.cards:
            print(c,end='\n',file=f)
