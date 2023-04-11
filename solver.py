import numpy as np 
import matplotlib as plot 

def print_board(bo):
    for i in range(len(bo)):
        if i % 3 == 0 and i != 0:
            print("-------------------------")
        if i == 0:
            print("_________________________")
        
        for j in range(len(bo[0])):
            if j == 0:
                print("| ", end="")
            if j % 3 == 0 and j != 0:
                print("| ", end="")

            if j == 8:
                print(f"{bo[i][j]} |")
            else:
                
                print(str(bo[i][j]) + " ", end="")
            
    print("-------------------------")
def valid(x, y, number, board):
    # global board
    for i in range(0, 9):
        if board[x][i] == number:
            return False
        if board[i][y] == number:
             return False
    gridx = (x//3) * 3
    gridy = (y//3) * 3
    for i in range(0,3):
            for j in range(0,3):
                if board[gridx + i][gridy + j] == number:
                    return False
    return True

def solve(board):
    """Board = 9x9 board
    X = Row number
    Y = Column number
    """
    for x in range(0,9):
        for y in range(0,9):
            if board[x][y] == 0:
                for i in range(1,10):
                    if valid(x,y,i, board):
                        board[x][y] = i
                        solve(board)
                        board[x][y] = 0
                return board
    print_board(board)
    

def main():
    #! Find a way to import the board into this array after classifying numbers in picture
    board = np.array([[7,8,0,4,0,0,1,2,0],
             [6,0,0,0,7,5,0,0,9],
             [0,0,0,6,0,1,0,7,8],
             [0,0,7,0,4,0,2,6,0],
             [0,0,1,0,5,0,9,3,0],
             [9,0,4,0,6,0,0,0,5],
             [0,7,0,3,0,0,0,1,2],
             [1,2,0,0,0,7,4,0,0],
             [0,4,9,2,0,6,0,0,7]])
    solve(board)


if __name__ == "__main__":
         main()