# Game: Black and White 2

## Rules
* Two players; Each player has 99 points in total.
* In each round:
    * First player input a number (integer, 0~available points).
        * If the number is between 0~9, it shows **black**; if it's >= 10, it shows **white**.
        * First player's indicator shows the rest of points falls within one of the range: 0-19, 20-39, 40-59, 60-79, 80-99.
    * Next player input a number (integer, 0~available points).
        * If the number is between 0~9, it shows **black**; if it's >= 10, it shows **white**.
        * Second player's indicator shows the rest of points falls within one of the range: 0-19, 20-39, 40-59, 60-79, 80-99.
    * Compare the input numbers from two players. Who inputs the larger number wins the round.
* Game ending condition:
    * Player who first wins 5 rounds wins.
    * If no player reaches 5 wins, the game ends after 9 rounds, and the player who wins more rounds wins.
* Sequence of each round:
    * In first round, randomly assign a player as first player.
    * After first round, the player who won last round will become first player in the new round.
