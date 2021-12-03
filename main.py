from game import Game
from player import Player

if __name__ == "__main__":
    player_1 = Player(input("Player 1 name: "))
    player_2 = Player(input("Player 2 name: "))
    game = Game(player_1, player_2)

    while True:
        game.startRound()
        game.decideFirstPlayer()
        game.letFirstPlayerAct()
        game.letSecondPlayerAct()
        game.checkOneRoundResult()
        game.checkGameResult()
