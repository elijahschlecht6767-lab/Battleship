import random
EMPTY_SPACE = "-"

def get_board(rows, cols):
    """this function creates the board based on coordinated inputted when called"""
    board = []
    for row in range(rows):
        board.append([])
        for col in range(cols):
            board[row].append(EMPTY_SPACE)
    return board


def print_board(board):
    """this function prints the board"""

    #assumes board has at least one row
    print("  ", end="")
    for i in range(len(board[0])):
        #this (chr) will take the number stored, add 65 to convert it to it's ascii value
        #eg. in memory "A" is stored as 65
        print(chr(i+65), end=" ")
    print()
    for idx, row in enumerate(board):
        print(idx, end=" ")
        for col in row:
            print(col, end=" ") #by default end=\n
        print()


def is_valid_coord(board, row, col):
    """assumes board has at least one row"""
    if not (0 <= row < len(board) and 0 <= col < len(board[0])):
        print("Invalid Coord")
        return False
    elif board[row][col] != EMPTY_SPACE:
        print("Space already fired on")
        return False
    return True


def player_ship(board):
    """this function asks the user to input where they want their ship to be and returns the info if it is a valid space"""

    while True:
        player1=input("Input the letter of the space you want your ship on -").strip().upper()
        if len(player1) != 1:
            print("invalid")
            continue
        player1=ord(player1)-65 #this makes player1 equal to its number equivelent
        player2=get_num_from_user("Input the number of the space you want your ship on -")

        is_valid=is_valid_coord(board, player1, player2)

        if is_valid:
            print(f"your coords: ({chr(player1+65)}, {player2})")
            return (player2, player1) #REPLACED BY SUGGESTION BY CHATGPT
        else:
            print("Please try again...")

def get_num_from_user(msg):
    while True:
        try:
            val = int(input(msg))
            return val
        except:
            print("try again")

def computer_ship(board, player_place):
    cpu1 = random.randint(0, len(board) - 1) #REPLACED BY SUGGESTION BY CHATGPT
    cpu2 = random.randint(0, len(board[0]) - 1) #REPLACED BY SUGGESTION BY CHATGPT

    is_valid=is_valid_coord(board, cpu1, cpu2)

    while True:
        if cpu1!=player_place[0] and cpu2!=player_place[-1] and is_valid:
            #print(f"cpu coords: ({chr(cpu1+65)}, {cpu2})")
            return (cpu1, cpu2) #REPLACED BY SUGGESTION BY CHATGPT
        else:
            cpu1 = random.randint(0, len(board) - 1) #REPLACED BY SUGGESTION BY CHATGPT
            cpu2 = random.randint(0, len(board[0]) - 1) #REPLACED BY SUGGESTION BY CHATGPT
            is_valid=is_valid_coord(board, cpu1, cpu2)


def cpu_strike(board, cpu_place, player_place):
    cpu1 = random.randint(0, len(board) - 1) #REPLACED BY SUGGESTION BY CHATGPT
    cpu2 = random.randint(0, len(board[0]) - 1) #REPLACED BY SUGGESTION BY CHATGPT

    if (cpu1==int(cpu_place[0]) and cpu2==int(cpu_place[-1])) or(board[cpu1][cpu2]!=EMPTY_SPACE and board[cpu1][cpu2]!="E"): #if either cpu1 or cpu2 are the same as cpu_place or if those coords are not equal to an empty space
        while True:
            cpu1 = random.randint(0, len(board) - 1) #REPLACED BY SUGGESTION BY CHATGPT
            cpu2 = random.randint(0, len(board[0]) - 1) #REPLACED BY SUGGESTION BY CHATGPT
            if not(cpu1==int(int(cpu_place[0])) and cpu2==int(int(cpu_place[-1]))) and(board[cpu1][cpu2]==EMPTY_SPACE or board[cpu1][cpu2]=="E"): #if cpu1 and cpu2 are not the same as cpu_place and if those coords are equal to an empty space
                break
    if (cpu1, cpu2) == player_place: #REPLACED BY SUGGESTION BY CHATGPT
        board[cpu1][cpu2]="O"
    else:
        board[cpu1][cpu2]="o"
    print(f"cpu target: {chr(cpu2+65)}, {cpu1}") #REPLACED BY SUGGESTION BY CHATGPT
    
    return board


def hints(board3, number, letter_as_num, cpu_place):
    if number>=cpu_place[0]:
        y_distance=number-cpu_place[0]
    elif number<cpu_place[0]:
        y_distance=cpu_place[0]-number

    if letter_as_num>=cpu_place[-1]:
        x_distance=letter_as_num-cpu_place[-1]
    elif letter_as_num<cpu_place[-1]:
        x_distance=cpu_place[-1]-letter_as_num

    if x_distance>y_distance:
        total_distance=x_distance
    else:
        total_distance=y_distance
    
    print(" ")
    print("?HINT?")
    print(" ")
    print(f"You are {total_distance} away from the cpu's ship...")

        

def main():
    #board=(
    #    ["A", "B", "C", "D", "E", "F", "G"],
    #    [0, 1, 2, 3, 4, 5, 6, 7]
    #)
    #board2=[
    #    ["-", "-", "-", "-", "-", "-", "-", "-"],
    #    ["-", "-", "-", "-", "-", "-", "-", "-"],
    #    ["-", "-", "-", "-", "-", "-", "-", "-"],
    #    ["-", "-", "-", "-", "-", "-", "-", "-"],
    #    ["-", "-", "-", "-", "-", "-", "-", "-"],
    #    ["-", "-", "-", "-", "-", "-", "-", "-"],
    #    ["-", "-", "-", "-", "-", "-", "-", "-"],
    #    ["-", "-", "-", "-", "-", "-", "-", "-"]
    #]

    #question=input("This game does not have the best error prevention system, actually, I didn't even intentially add one at all, continie to the game? (Y/N) ").strip().lower()
    #if question=="y":
    #    print("Great, here we go!")
    #elif question=="n":
    #    print("Too bad.")
    #else:
    #    print("That was invalid input, idk what it means but here we go ig.")

    hint=False
    board3 = get_board(8,8)
    print_board(board3)
    player_place=player_ship(board3)
    board3[player_place[00]][player_place[1]] = "E" #REPLACED BY SUGGESTION BY CHATGPT
    print("The \"E\" is your ship")
    cpu_place=computer_ship(board3, player_place)

    print("For testing purposes; the cpu's ship placement is the following")
    print(f"{chr(int(cpu_place[1])+65)}, {cpu_place[0]}") #REPLACED BY SUGGESTION BY CHATGPT

    #board3[1][2] = "X"
    while True:
        print_board(board3)
        while True:
            letter=str(input("input the letter of the space you want to strike here (use this prompt to turn on hint if you want) -"))
            if len(letter) != 1 and letter.count("hint") != 1:
                print("invalid")
                continue
            if letter=="hint=1":
                hint=True
            elif letter=="hint=0":
                hint=False
            else:
                letter=letter.strip().upper()[0] #assumes at least one char
                break
        number= get_num_from_user("input the number of the space you want to strike here -")
        letter_as_num = (ord(letter)-65)

        is_valid=is_valid_coord(board3, number, letter_as_num)
        #print(is_valid_coord(board3, number, letter_as_num))
        #print(len(board3))
        #print(len(board3[0]))

        if is_valid:
            if (number, letter_as_num) == cpu_place: #if the place you are aiming for is equal to the cpu's ship #REPLACED BY SUGGESTION BY CHATGPT
                #print(f"your number and letter as number: {number}, {letter_as_num}, and the cpu's number and letter as a number: {int(cpu_place[0])}, {int(cpu_place[-1])}")
                print("Hit")
                board3[number][letter_as_num]="X" #sets the mark you are aiming for to "X"
                print_board(board3)
                print("You won!")
                break
            else:
                print("Miss")
                print(" ")
                board3[number][letter_as_num]="x" #sets the mark you are aiming for to "x"

        else: #if the place you aimed for is invalid, it will keep asking you to redo untill you input valid coords
            while True:
                print_board(board3)
                print("Please try again...")
                print("")
                while True:
                    letter=input("input the letter of the space you want to strike here (use this prompt to turn on hint if you want) -")
                    if len(letter) != 1 and letter.count("hint") != 1:
                        print("invalid")
                        continue
                    if letter=="hint=1":
                        hint=True
                    elif letter=="hint=0":
                        hint=False
                    else:
                        letter=letter.strip().upper()[0] #assumes at least one char
                        break
                number=int(input("input the number of the space you want to strike here -"))
                letter_as_num = (ord(letter)-65)

                is_valid=is_valid_coord(board3, number, letter_as_num)

                if is_valid:
                    if board3[number][letter_as_num]==board3[int(cpu_place[0])][int(cpu_place[-1])]: #if the place you are aiming for is equal to the cpu's ship
                        print("Hit")
                        board3[number][letter_as_num]="X" #sets the mark you are aiming for to "X"
                        print_board(board3)
                        print("You won!")
                        break
                    else:
                        print("Miss")
                        print(" ")
                        board3[number][letter_as_num]="x" #sets the mark you are aiming for to "x"
                        break
            if board3[number][letter_as_num]==board3[int(cpu_place[0])][int(cpu_place[-1])]:
                break
        
        if hint:
            hints(board3, number, letter_as_num, cpu_place)
        
        print("cpu turn:")
        board3=cpu_strike(board3, cpu_place, player_place) #this is a new addition

        if board3[int(player_place[0])][int(player_place[-1])]=="O":
            print("You lost...")
            break

    #Get index of "A"

    #this will take a character such as "A" and convert it to a number starting at 0
    #moving it to 0 so it aligns with the index. 
    #print(ord("C")-65) #this is actually 2

    #board2[2][2]="x"


#challenge - add an option to type hint=1 (or hint=0)
#if hint is 1, after each shot say about how far away you are. 

if __name__ == "__main__":
    main()
 
# My Goal:
"""

#####
EVERYTHING PAST THIS POINT WAS ON A TEMPLATE I AM NOT REQUIRED TO FOLLOW
#####

Create a grid that looks like this:
  A B C D E F G H
0 - - - - - - - -
1 - - - - - - - -
2 - - - - - - - -
3 - - - - - - - -
4 - - - - - - - -
5 - - - - - - - -
6 - - - - - - - -
7 - - - - - - - -
 
Prompt user for coordinates to place their ship
 
Have the computer choose a random space to be it's ship (keep hidden)
 
Prompt user for coordinates (eg. A1)
Fire a shot on that coordinate
 
If the computers ship is hit, report the win
Otherwise, allow the computer to fire a shot at your ship
If your ship is hit, report the computer win
Game Over
"""