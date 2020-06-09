board={1:' ',2:' ',3:' ',4:' ',5:' ',6:' ',7:' ',8:' ',9:' '}

player=1            #to initialize player1
total_moves=0           #this should not exceed 9
end=0

def  check():
    #moves of player one
    # for horizontal conditions
    if board[1] =="X" and board[2] =="X" and board[3] =="X":
        print("Player 1 won!")
        return 1
    if board[4]=="X" and board[5]=="X" and board[6]=="X":
        print("Player 1 won!")
        return 1
    if board[7]=="X" and board[8]=="X" and board[9]=="X":
        print("Player 1 won!")
        return 1
    # horizontal conditions checked
    #diagonal conditions
    if board[1]=="X" and board[5]=="X" and board[9]=="X":
        print("Player 1 won!")
        return 1
    if board[3]=="X" and board[5]=="X" and board[7]=="X":
        print("Player 1 won!")
        return 1
    # diagonal conditions checked
    #vertical conditions
    if board[1]=="X" and board[4]=="X" and board[7]=="X":
        print("Player 1 won!")
        return 1
    if board[2]=="X" and board[5]=="X" and board[8]=="X":
        print("Player 1 won!")
        return 1
    if board[3]=="X" and board[6]=="X" and board[9]=="X":
        print("Player 1 won!")
        return 1

        # vertical conditions checked

    # player 2
        # for horizontal conditions
        if board[1] == "O" and board[2] == "O" and board[3] == "O":
            print("Player 2 won!")
            return 1
        if board[4] == "O" and board[5] == "O" and board[6] == "O":
            print("Player 2 won!")
            return 1
        if board[7] == "O" and board[8] == "O" and board[9] == "O":
            print("Player 2 won!")
            return 1
        # horizontal conditions checked
        # diagonal conditions
        if board[1] == "O" and board[5] == "O" and board[9] == "O":
            print("Player 2 won!")
            return 1
        if board[3] == "O" and board[5] == "O" and board[7] == "O":
            print("Player 2 won!")
            return 1
        # diagonal conditions checked
        # vertical conditions
        if board[1] == "O" and board[4] == "O" and board[7] == "O":
            print("Player 2 won!")
            return 1
        if board[2] == "O" and board[5] == "O" and board[8] == "O":
            print("Player 2 won!")
            return 1
        if board[3] == "O" and board[6] == "O" and board[9] == "O":
            print("Player 2 won!")
            return 1

            # vertical conditions checked
        return 0

print('1|2|3')
print('-+-+-')
print('4|5|6')
print('-+-+-')
print('7|8|9')
print("*******************************************************")

while True:
    print(board[1]+'|'+board[2]+'|'+board[3])
    print('-+-+-')
    print(board[4] + '|' + board[5] + '|' + board[6])
    print('-+-+-')
    print(board[7] + '|' + board[8] + '|' + board[9])
    end=check()
    if total_moves ==9 or end==1:
        break
    while True:
        if player ==1:
            p1 = int(input("player 1 :"))
            if p1 in board and board[p1]==" ":
                board[p1]="X"
                player=2
                break
            else:
                print("Invalid input,try again")
                continue
        else:
            p2=int(input("player 2 :"))
            if p2 in board and board[p2]==" ":
                board[p2]="O"
                player=1
                break
            else:
                print("Invalid input,try again")
                continue
    total_moves +=1
    print("******************************************************")
    print()
