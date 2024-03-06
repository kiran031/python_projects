import time
board = [" "for i in range(0,9)]

def table():
    print()
    print(f"|{board[0]}|{board[1]}|{board[2]}|")
    print(f"|{board[3]}|{board[4]}|{board[5]}|")
    print(f"|{board[6]}|{board[7]}|{board[8]}|")
    print()

def player_move(icon):
    if icon == "X":
        number = 1
    elif icon == "O":
        number = 2

    print(f"now number {number} player move")
    choice = int(input("Enter the number (1-9):").strip())
    if(board[choice-1] == " "):
       board[choice-1] = icon
    else:
        print()
        print("that space is alredy taken!")
        print("----------------------------")

def is_victory(icon):
    if (board[0]==icon and board[1]==icon and board[2]== icon) or\
       (board[3]==icon and board[4]==icon and board[5]== icon) or\
       (board[6]==icon and board[7]==icon and board[8]== icon) or\
       (board[0]==icon and board[4]==icon and board[8]== icon) or\
       (board[2]==icon and board[4]==icon and board[6]== icon) or\
       (board[0]==icon and board[3]==icon and board[6]== icon) or\
       (board[1]==icon and board[4]==icon and board[7]== icon) or\
       (board[2]==icon and board[5]==icon and board[8]== icon):
        return True
    else:
        return False


def is_draw(icon):
    if " " not in board:
        return True
    else:
        return False
       

while True:
    table()
    player_move("X")
    table()
    if is_victory("X"):
        time.sleep(3)
        print(f"congrajulation...player X won the match")
        break
    elif is_draw("X"):
        print("ooo....Match is draw")
        break
    player_move("O")
    if is_victory("O"):
        table()
        time.sleep(3)
        print(f" congarjulation...player O won the match")
        break;
    elif is_draw("O"):
        print("ooo....Match is draw")
        break
    
   
    
        
    
          