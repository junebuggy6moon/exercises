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
while who_won() == "Nobody":
    print_board()
    answer1 = input("Player 1, please enter a coordinate from each.")
    answer2 = input("Player 2, please enter a coordinate from each.")

    answer1_h = int(answer1.split(",")[0]) -1
    answer1_v = int(answer1.split(",")[1]) -1

    game[answer1_h][answer1_v] = 1

    answer2_h = int(answer2.split(",")[0]) -1
    answer2_v = int(answer2.split(",")[1]) -1

    game[answer2_h][answer2_v] = 2

if who_won() == "P1" or who_won() == "P2":
    print(f"{who_won()} you won!")
    print_board()

