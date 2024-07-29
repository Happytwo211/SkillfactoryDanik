print("Hello! welcome to the sea battle")
import random
class Logic:
    pass
#как куда и где и сколько ходить и звачем

class GameBoard:
    def __init__(self, size):
        self.size = 6
        self.field =[[["0"] for i in range(self.size)] for j in range(self.size)]
        # self.field=[x][y]
    def disp_board(self):
        res = ""
        res += "  | 1 | 2 | 3 | 4 | 5 | 6 |"
        for i, row in enumerate(self.field):
            res += f"\n{i+1} | " + " | ".join(row) + " |"

class AIMoves(GameBoard):
    def moves(self):
        self.field[x][y]=random.randint(0,5), random.randint(0,5)
        # print(f"AI move is {self.field}")
# class AvaibleMove(AIMoves):
#     def avaivble_move(self):
#         if self.field[x][y] != "0":
#             return avaivble_move

class Coordinate:
    def __init__(self, x , y ):
        self.x = x
        self.y = y
    def __repr__(self):
        return {self.x}, {self.y}

class Ship(Coordinate):
    # def __init__(self, x , y):
        pass


