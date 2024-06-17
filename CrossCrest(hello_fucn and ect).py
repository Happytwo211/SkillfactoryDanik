#game_field=[""]*9
def say_hello():
    print("Hello, enter the name of two players")
    player1=input("enter the name of 1st player")
    print("Player#1-", player1, "use cross")
    player2=input("enter the name of 2nd player")
    print("Player#2-", player2 , "use zeros")

def read_rules():
    print("RULES:")
    rules=['1)Players make moves one by one.' , '2)Player win in case he has 3 same symbols in the line, ether vertical,horizontal,or diogonal' , '3)Type coordintaes x,y for moves(x-strings, y-colums ']
    print(*rules)
def is_ready():
    ready_or_not=str(input("enter ''!ready'' if you ready to play"))
    ready_or_not.replace("  ","")
    gamestart = ready_or_not == "!ready"
    if gamestart:
        print("players are ready, game stars in 3...2...1...GO!")
    else:
        print("players are not ready, game will not be started")
        return is_ready()




def show_battlefiedl():
    print("Chose coordinates to place your symbole (x,y) : ")
    game_field=[[" "] * 3 for i in range(3)]
    print(f"   1  2  3")
    for i in range(3):
        row_join=" ".join(game_field[i])
        print(f"{i} {game_field[i][0]} {game_field[i][1]} {game_field[i][2]}")

say_hello()
is_ready()
read_rules()
show_battlefiedl()








