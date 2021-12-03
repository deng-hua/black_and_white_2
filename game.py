import getpass
import random


class Game:
    def __init__(self, player_1, player_2):
        self.round = 0
        self.player_dict = {1: player_1, 2: player_2}
        self.first_player = None
        self.second_player = None
        self.first_player_history = []
        self.second_player_history = []
        self.player_used_points_dict = {1: [], 2: []}
        self.win_history = []
        self.win_mapping = {
            1: f"{self.player_dict[1].name}'s win",
            2: f"{self.player_dict[2].name}'s win",
            999: "Draw",
        }

    def startRound(self):
        self.round += 1
        print("--------------------")
        print(f"##### Round {self.round} #####")
        print("--------------------")

    def decideFirstPlayer(self):
        if (self.round == 1) or (self.win_history[-1] == 999):
            number = random.randint(1, 2)
            self.first_player = number
            self.second_player = 3 - number
        else:
            win_number = self.win_history[-1]
            self.first_player = win_number
            self.second_player = 3 - win_number
        self.first_player_history.append(self.first_player)
        self.second_player_history.append(self.second_player)

    def letFirstPlayerAct(self):
        print(f"{self.player_dict[self.first_player].name}'s turn:")
        print(
            f"Your total points are: {self.player_dict[self.first_player].points}",
        )
        used_points = int(getpass.getpass("Use points:"))
        print("\033[A                                             \033[A")
        print("\033[A                                             \033[A")
        self.player_dict[self.first_player].usePoints(used_points)
        self.player_used_points_dict[self.first_player].append(used_points)
        self.player_dict[self.first_player].displayLeftPointsIndicator()
        print("--------------------")

    def letSecondPlayerAct(self):
        print(f"{self.player_dict[self.second_player].name}'s turn:")
        print(
            f"Your total points are: {self.player_dict[self.second_player].points}",
        )
        used_points = int(getpass.getpass("Use points:"))
        print("\033[A                                             \033[A")
        print("\033[A                                             \033[A")
        self.player_dict[self.second_player].usePoints(used_points)
        self.player_used_points_dict[self.second_player].append(used_points)
        self.player_dict[self.second_player].displayLeftPointsIndicator()
        print("--------------------")

    def checkOneRoundResult(self):
        if (
            self.player_used_points_dict[self.first_player][-1]
            > self.player_used_points_dict[self.second_player][-1]
        ):
            win_number = self.first_player
        elif (
            self.player_used_points_dict[self.first_player][-1]
            < self.player_used_points_dict[self.second_player][-1]
        ):
            win_number = self.second_player
        else:
            win_number = 999
        print(f"Round {self.round}: {self.win_mapping[win_number]}")
        self.win_history.append(win_number)

    def checkGameResult(self):
        if (
            (self.round == 9)
            or (self.win_history.count(1) == 5)
            or (self.win_history.count(2) == 5)
        ):
            self.endGame()

    def endGame(self):
        print("#### Game End ####")
        if self.win_history.count(1) > self.win_history.count(2):
            print(self.win_mapping[1])
        if self.win_history.count(1) < self.win_history.count(2):
            print(self.win_mapping[2])
        if self.win_history.count(1) == self.win_history.count(2):
            print(self.win_mapping[999])
        for i in range(self.round):
            print("----------------")
            print(f"Round {i+1}: {self.win_history[i]}")
            print(
                f"""{self.player_dict[self.first_player_history[i]].name}:
                {self.player_used_points_dict[self.first_player_history[i]][i]}""",
            )
            print(
                f"""{self.player_dict[self.second_player_history[i]].name}:
                {self.player_used_points_dict[self.second_player_history[i]][i]}""",
            )
        exit()
