

def parse(raw):
    player1, player2 = raw.split('\n\n')
    p1_deck = [int(x) for x in player1.split('\n')[1:]]
    p2_deck = [int(x) for x in player2.split('\n')[1:]]
    return p1_deck, p2_deck


def game(p1_deck, p2_deck, rounds):
    while(p1_deck and p2_deck):
        if (p1_deck, p2_deck) in rounds:
            return p1_deck, 1
        rounds.append((p1_deck.copy(),p2_deck.copy()))
        p1_card = p1_deck.pop(0)
        p2_card = p2_deck.pop(0)

        if p1_card > len(p1_deck) or p2_card > len(p2_deck):
            if(p1_card > p2_card):
                p1_deck.append(p1_card)
                p1_deck.append(p2_card)
            else:
                p2_deck.append(p2_card)
                p2_deck.append(p1_card)
        else:
            _, win_id = game(p1_deck[:p1_card].copy(), p2_deck[:p2_card].copy(), rounds=[])
            if win_id == 1:
                p1_deck.append(p1_card)
                p1_deck.append(p2_card)
            else:
                p2_deck.append(p2_card)
                p2_deck.append(p1_card)    
    winner_deck, winner_id = (p1_deck, 1) if len(p2_deck) == 0 else (p2_deck, 2)
    return winner_deck, winner_id


if __name__ == '__main__':
    with open('input') as f:
        data = f.read()
    p1_deck, p2_deck = parse(data)
    winner_deck, num = game(p1_deck,p2_deck,[])
    result = 0
    print(winner_deck,num)
    for z, card in enumerate(reversed(winner_deck), 1):
        result += z*card
    print(result)
