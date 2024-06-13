game_field=[""]*9
print("Hello, enter the name of two players")
player1=input("enter the name of 1st player")
print("Player#1-",player1)
player2=input("enter the name of 2nd player")
print("Player#2-",player2)
ready_or_not = input("enter ''!ready'' if you ready to play")
gamestart = ready_or_not == "!ready"
def is_ready():
    if gamestart:
        print("players are ready, game stars in 3...2...1...GO!")
    else:
        print("players are not ready, game will not be started")
        return is_ready()
is_ready()
