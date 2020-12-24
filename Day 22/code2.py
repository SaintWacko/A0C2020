import os


def main():

    def combat(player1, player2, level=0):
        # print(level)
        history = [(player1[:], player2[:])]
        while player1 and player2:
            card1 = player1.pop(0)
            card2 = player2.pop(0)
            if len(player1) >= card1 and len(player2) >= card2:
                winner, deck = combat(player1[:card1], player2[:card2], level + 1)
            else:
                winner = 1 if card1 > card2 else 2
            if winner == 1:
                player1.append(card1)
                player1.append(card2)
            else:
                player2.append(card2)
                player2.append(card1)
            if (player1, player2) in history:
                return (1, player1)
            history.append((player1[:], player2[:]))
        return (1, player1) if player1 else (2, player2)
        print(player1)
        print(player2)

    players = []
    with open(os.path.join(os.path.dirname(os.path.abspath(__file__)), 'input'), 'r') as file:
        players = file.read().split('\n\n')
    player1 = [int(card) for card in players[0].splitlines()[1:]]
    player2 = [int(card) for card in players[1].splitlines()[1:]]
    winner, deck = combat(player1, player2)
    deck = [(idx + int(1)) * card for idx, card in enumerate(deck[::-1])]
    return sum(deck)



if __name__ == "__main__":
    print(main())
