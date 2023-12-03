game = [[0, 0, 0],
	    [0, 0, 0],
	    [0, 0, 0]]

def vertical(size, v):
    vertical_line = "|"
    for h in range(size):
        vertical_line += f" {game[v][h]} |"
    print(vertical_line)
def who_won():
    if game[0][0] == game[0][1] == game[0][2] == 1:
        return("P1")
    if game[0][0] == game[0][1] == game[0][2] == 2:
        return("P2")

    if game[0][0] == game[1][0] == game[2][0] == 1:
        return("P1")
    if game[0][0] == game[1][0] == game[2][0] == 2:
        return("P2")

    if game[2][0] == game[2][1] == game[2][2] == 1:
        return("P1")
    if game[2][0] == game[2][1] == game[2][2] == 2:
        return("P2")

    if game[0][2] == game[1][2] == game[2][2] == 1:
        return ("P1")
    if game[0][2] == game[1][2] == game[2][2] == 2:
        return ("P2")

    if game[0][1] == game[1][1] == game[2][1] == 1:
        return("P1")
    if game[0][1] == game[1][1] == game[2][1] ==2:
        return("P2")

    if game[1][0] == game[1][1] == game[1][2] == 1:
        return("P1")
    if game[1][0] == game[1][1] == game[1][2] == 2:
        return("P2")

    if game[0][0] == game[1][1] == game[2][2] == 1:
        return("P1")
    if game[0][0] == game[1][1] == game[2][2] == 2:
        return("P2")

    if game[2][0] == game[1][1] == game[0][2] == 1:
        return("P1")
    if game[2][0] == game[1][1] == game[0][2] == 2:
        return ("P2")

    return("Nobody")


def horizontal(size):
    horizontal_line = ""
    for h in range(size):
        horizontal_line += " ---"
    print(horizontal_line)

def print_board():
    size = len(game)
    horizontal(size)
    for v in range(size):
        vertical(size, v)
        horizontal(size)

#ask player1 to enter in coordinate
#ask player2 to enter in coordinate
#they can't overwrite each other
#use a while loop if no one is wining then keep looping until someone does or tie.

player = "P1"
while who_won() == "Nobody":
    print_board()

    answer = input(f"{player}, please enter a coordinate from each.")

    answer_h = int(answer.split(",")[0]) -1
    answer_v = int(answer.split(",")[1]) -1

    if player == "P1":
        game[answer_h][answer_v] = 1
    elif player == "P2":
        game[answer_h][answer_v] = 2

    if player == "P1":
        player = "P2"
    elif player == "P2":
        player = "P1"

if who_won() == "P1" or who_won() == "P2":
    print(f"{who_won()} you won!")
    print_board()
