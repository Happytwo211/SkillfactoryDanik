game_field=[[" "] * 3 for i in range(3) ]
def hello():
    print("Hello, enter name of 2 players")
    playe1=input("Type the 1st player name")
    playe2 = input("Type the 2nd player name")
    print(f" {playe1} uses crosses")
    print(f" {playe2} uses zeros")


def read_rules():
    print("RULES:")
    print("Players make moves one by one")
    print("Player win in case he has 3 same symbols in the line, ether vertical,horizontal,or diogonal")

read_rules()
def is_ready():
    ready_or_not=str(input("Type ''!ready'' if you ready to play"))
    gamestart = ready_or_not == "!ready"
    if gamestart:
        print("Players are ready")
        print("Game starts in 3...")
        print("2...")
        print("1...")
        print("GO!")
    else:
        print("Players are not ready, game will not be started")
        return is_ready()

is_ready()

def show_battlefiedl():
    print("Chose coordinates to place your symbole (x,y) : ")
    game_field=[[" "] * 3 for i in range(3)]
    print(f"  | 1 | 2 | 3 |")
    for i in range(3):
        row_join=" ".join(game_field[i])
        print(f"{i} | {game_field[i][0]} | {game_field[i][1]} | {game_field[i][2]} |")


def player_moves():
    while True:
        cords = input("Type 2 coordinates in format [x,y] ").split()

        if len(cords) != 2:
            print("Type 2 coordinates!")
            continue

        x, y = cords

        if not(x.isdigit) or not(y.isdigit):
            print("X and Y has to be a numbers ")
            continue

        x, y = int(x), int(y)

        if x<0 or x>2 or y<1 or y>3:
            print("Coordinates is not in range of the battlefield")
            continue

        if game_field[x][y] != " ":
            print("Choose a free spot")

        if not int(x) or not int(y):
            print("Enter int numbers")

        return x,y

def if_win():
    win_comb = (((0, 0), (0, 1), (0, 2)),
                ((1, 0), (1, 1), (1, 2)),
                ((2, 0), (2, 1), (2, 2)),
                ((0, 2), (1, 1), (2, 0)),
                ((0, 0), (1, 1), (2, 2)),
                ((0, 0), (1, 0), (2, 0)),
                ((0, 1), (1, 1), (2, 1)),
                ((0, 2), (1, 2), (2, 2)))
    for cord in win_comb:
        symbols=[]
        for i in cord:
            symbols.append(game_field[i[0]][i[1]])
            if symbols==["X","X","X"]:
                print("X-is a winner")
            if symbols==["Y","Y","Y"]:
                print("Y-is a winner")

hello()
player_moves()

while True:
    count_moves=0
    if count_moves==0:
        print("X to move")
        count_moves+=1

    if count_moves%2==1:
        print("X to move")
        count_moves+=1
    else:
        print("Y to move")
        count_moves += 1

    x, y = game_field

    if count_moves%2==1:
        game_field[x][y]
        if count_moves % 2 == 1:
            game_field[x][y] = "X"
        else:
            game_field[x][y] = "0"

        if if_win():
            break

        if count_moves == 9:
            print(" Ничья!")
            break









