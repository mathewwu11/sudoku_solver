# Python Sudoku Solver
# Allows user to enter or create sudoku puzzle
# Will solve puzzle if possible and will notify user if the puzzle is impossible

import sys


# Prints a neater version of the sudoku board using - for horizontal parts of the grid and using | for vertical parts
# Alternatives to using this are using a matrix method in numpy, but I preferred this method as it looked a bit nicer to
# read as a sudoku board
def fancy_print(board):
    for i in range(len(board)):
        if i % 3 == 0 and i != 0:
            print("- - - - - - - - - - - - -")

        for j in range(len(board[0])):
            if j % 3 == 0 and j != 0:
                print(" | ", end="")

            if j == 8:
                print(board[i][j])
            else:
                print(str(board[i][j]) + " ", end="")


# Function finds an empty position (row index, column index)
# Function reads from right to left before going to next line
# *Note*: Playable numbers in sudoku are 1-9, so this solver uses 0 as a placeholder to represent an empty square
def find_empty(board):
    for i in range(len(board)):
        for j in range(len(board[0])):
            if board[i][j] == 0:
                return (i, j)
    return None


# Function is given a board state, a selected position, and a number to be tested in that selected position
# With this information, the function determines if the board state is valid within the rules of sudoku
def check_valid(board, number, position):
    # Checks row (Sweeps from left to right)
    for i in range(len(board[0])):
        if board[position[0]][i] == number and position[1] != i:
            return False
    # Checks column (Sweeps from top to bottom)
    for j in range(len(board)):
        if board[j][position[1]] == number and position[0] != j:
            return False

    # Checks box (3x3 grid of positions)
    box_x = position[1] // 3
    box_y = position[0] // 3

    for i in range(box_y * 3, box_y * 3 + 3):
        for j in range(box_x * 3, box_x * 3 + 3):
            if board[i][j] == number and (i, j) != position:
                return False

    return True


# Solves sudoku board using backtracking
# Notifies user if given puzzle has no solution
def solve(board):

    # purpose of count variable is described in the main function
    global count
    find = find_empty(board)
    if not find:
        return True
    else:
        row, col = find

    # checking for all numbers allowed to be placed in a block
    for i in range(1, 10):
        if check_valid(board, i, (row, col)):

            board[row][col] = i
            count += 1
            if count == 999:
                print("Unsolvable 💀\n"
                      "You really taking the L + ratio on this on ong")
                return False
            if solve(board):
                count = 0
                return True

            board[row][col] = 0
    print("L moment")
    return False


# Main Function

# Instructions
print("Hello! Welcome to Python Sudoku Solver!\n"
      "Please enter your puzzle in the format that follows:\n"
      "Columns are given a label of A-I\n"
      "Rows are given a label of 1-9\n"
      "Please enter the number found in the box, followed by the box row location,"
      "then by the box column location\n"
      "Ex. The input 1A2 would place the number 1 in the box A2:\n"
      "   A B C    D E F    G H I \n"
      "1  0 0 0  | 0 0 0  | 0 0 0\n"
      "2  1 0 0  | 0 0 0  | 0 0 0\n"
      "3  0 0 0  | 0 0 0  | 0 0 0\n"
      "   - - - - - - - - - - - - -\n"
      "4  0 0 0  | 0 0 0  | 0 0 0\n"
      "5  0 0 0  | 0 0 0  | 0 0 0\n"
      "6  0 0 0  | 0 0 0  | 0 0 0\n"
      "   - - - - - - - - - - - - -\n"
      "7  0 0 0  | 0 0 0  | 0 0 0\n"
      "8  0 0 0  | 0 0 0  | 0 0 0\n"
      "9  0 0 0  | 0 0 0  | 0 0 0\n"
      "Once you have entered one box you will be prompted for another\n"
      "Once you have entered all the boxes of your puzzle, enter three 0's (000) to quit setup and to "
      "solve the puzzle\n"
      "To preview the puzzle, type 'PREVIEW'\n")

while True:
    # Sets the board empty
    puzzle = [[0, 0, 0, 0, 0, 0, 0, 0, 0],
              [0, 0, 0, 0, 0, 0, 0, 0, 0],
              [0, 0, 0, 0, 0, 0, 0, 0, 0],
              [0, 0, 0, 0, 0, 0, 0, 0, 0],
              [0, 0, 0, 0, 0, 0, 0, 0, 0],
              [0, 0, 0, 0, 0, 0, 0, 0, 0],
              [0, 0, 0, 0, 0, 0, 0, 0, 0],
              [0, 0, 0, 0, 0, 0, 0, 0, 0],
              [0, 0, 0, 0, 0, 0, 0, 0, 0]]

    # count variable is used to for class in which the board is in a unsolvable state
    # While it is possible to just allow the program recursively run through every single possible board state,
    # there is a very large number of possible board states that it would need to check through
    # Using a count variable, an arbitrary limit can be set (in the case of this program it is 999) that is large
    # enough that after the program runs through that many board states without finding a single input that it is
    # reasonable to assume that the puzzle is unsolvable
    # This also means that the program will not lag if given an unsolvable puzzle
    count = 0

    user_input = input("> ")
    while True:

        # Expects user to input a three character code (number/letter/number) to indicate the position and number
        if len(user_input) == 3:

            # User done with inputting
            if user_input == "000":
                break

            user_input = list(user_input)

            number = user_input[0]
            col = str(user_input[1])
            row = user_input[2]

            if number.isdigit() or number is int:
                number = int(number)
            else:
                print("You messed up buddy 💀")
                number = None

            if row.isdigit() or row is int:
                row_index = int(row) - 1
            else:
                print("You messed up buddy 💀")
                row_index = None

            if col.upper() == "A":
                col_index = 0
            elif col.upper() == "B":
                col_index = 1
            elif col.upper() == "C":
                col_index = 2
            elif col.upper() == "D":
                col_index = 3
            elif col.upper() == "E":
                col_index = 4
            elif col.upper() == "F":
                col_index = 5
            elif col.upper() == "G":
                col_index = 6
            elif col.upper() == "H":
                col_index = 7
            elif col.upper() == "I":
                col_index = 8
            else:
                col_index = None
                print("You messed up buddy 💀")

            # insures the input is valid
            if row_index is not None and col_index is not None and number is not None:
                puzzle[row_index][col_index] = number

        # Gives a preview of the board
        elif str(user_input).upper() == "PREVIEW":
            fancy_print(puzzle)

        # Covers if the user inputs does not follow the format given in the instructions
        else:
            print("You messed up buddy 💀")

        user_input = input("Next input\n"
                           "> ")

    # prints the unsolved puzzle board and the solved puzzle board if a solution exists
    print("Unsolved Puzzle\n")
    fancy_print(puzzle)
    solve(puzzle)
    if solve(puzzle):
        print("\nSolved Puzzle\n")
        fancy_print(puzzle)

    continue_playing = ""
    failed_yes_or_no = 0

    # checks whether the user wants to continue playing
    # program will quit on the 6th invalid input from the user
    print("Continue playing? (Yes or No)")

    while True:
        continue_playing = input("> ")
        if continue_playing.upper() == "YES" or continue_playing.upper() == "NO":
            break
        failed_yes_or_no += 1
        if failed_yes_or_no == 1:
            print("Invalid Input")
        if failed_yes_or_no == 2:
            print("Really bro?")
        if failed_yes_or_no == 3:
            print("I can do this all day")
        if failed_yes_or_no == 4:
            print("Can you just, like, pick yes or no already? 😠")
        if failed_yes_or_no == 5:
            print("Alright if you do this one more time, I swear to god")
        if failed_yes_or_no == 6:
            print("*Terminates one's self*")
            sys.exit()

    if continue_playing.upper() == "NO":
        break

    if continue_playing.upper() == "YES":
        print("Board Reset\n"
              "Please enter your board information, one square at a time")

sys.exit()
