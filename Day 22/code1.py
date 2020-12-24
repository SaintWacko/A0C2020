import os


def main():
    players = []
    with open(os.path.join(os.path.dirname(os.path.abspath(__file__)), 'input'), 'r') as file:
        players = file.read().split('\n\n')
    player1 = [int(card) for card in players[0].splitlines()[1:]]
    player2 = [int(card) for card in players[1].splitlines()[1:]]
    while player1 and player2:
        card1 = player1.pop(0)
        card2 = player2.pop(0)
        if card1 > card2:
            player1.append(card1)
            player1.append(card2)
        if card2 > card1:
            player2.append(card2)
            player2.append(card1)
    print(player1)
    print(player2)
    winner = player1 if player1 else player2
    winner = [(idx + int(1)) * card for idx, card in enumerate(winner[::-1])]
    return sum(winner)



if __name__ == "__main__":
    print(main())
