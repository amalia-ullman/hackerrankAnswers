# if a cell has less than 2 neighbors it dies
# if a cell has 2-4 neighbors it lives
# if a dead cell has 3 neighbors it comes back to life
# if a cell has 5 or more neighbors it dies

from time import sleep
from termcolor import colored

d = colored("-", "red")
O = colored("O", "magenta")

board = [
    [d, d, d, d, d, d, d, d, d, d, d, d],
    [d, d, O, d, d, d, d, d, d, d, d, d],
    [d, d, d, O, O, d, d, d, d, d, d, d],
    [d, d, O, O, d, d, d, d, d, d, d, d],
    [d, d, d, d, d, d, d, d, d, d, d, d],
    [d, d, d, d, d, d, d, d, d, d, d, d]
]

def printBoard(list):
    for row in range(len(list)):
        print("-----------------------")
        currentrow = ""
        for column in range(len(list[row])):
            currentrow += str(list[row][column]) + " "
        print(currentrow)
    print("-----------------------")
printBoard(board)

def generateBored(list):
    newboard = [
        [d, d, d, d, d, d, d, d, d, d, d, d],
        [d, d, d, d, d, d, d, d, d, d, d, d],
        [d, d, d, d, d, d, d, d, d, d, d, d],
        [d, d, d, d, d, d, d, d, d, d, d, d],
        [d, d, d, d, d, d, d, d, d, d, d, d],
        [d, d, d, d, d, d, d, d, d, d, d, d]
    ]
    for row in range(len(list)):
        for column in range(len(list[row])):
            neighbors = 0
            if(row == 0):
                if(column == 0):
                    if(list[row][column + 1] == O):
                        neighbors += 1
                    if(list[row + 1][column] == O):
                        neighbors += 1
                    if(list[row + 1][column + 1] == O):
                        neighbors += 1
                elif(column < len(list[row])-1):
                    if(list[row][column + 1] == O):
                        neighbors += 1
                    if(list[row][column - 1] == O):
                        neighbors += 1
                    if(list[row + 1][column - 1] == O):
                        neighbors += 1
                    if(list[row + 1][column] == O):
                        neighbors += 1
                    if(list[row + 1][column + 1] == O):
                        neighbors += 1
                    #if(row < len(list)-1):
                        #if(list[row + 1][column + 1] == O):
                            #neighbors += 1
                            #print("hello also a person")
                elif(column == len(list[row])-1):
                    if(list[row][column - 1] == O):
                        neighbors += 1
                    if(list[row + 1][column - 1] == O):
                        neighbors += 1
                    if(list[row + 1][column] == O):
                        neighbors += 1
            elif(row != 0 and row < len(list) -1):
                if(column == 0):
                    if(list[row][column + 1] == O):
                        neighbors += 1
                    if(list[row + 1][column] == O):
                        neighbors += 1
                    if(list[row + 1][column + 1] == O):
                        neighbors += 1
                    if(list[row - 1][column] == O):
                        neighbors += 1
                    if(list[row - 1][column + 1] == O):
                        neighbors += 1
                elif(column != 0 and column < len(list[row])-1):
                    if(list[row - 1][column - 1] == O):
                        neighbors += 1
                    if(list[row - 1][column] == O):
                        neighbors += 1
                    if(list[row - 1][column + 1] == O):
                        neighbors += 1
                    if(list[row][column - 1] == O):
                        neighbors += 1
                    if(list[row][column + 1] == O):
                        neighbors += 1
                    if(list[row + 1][column - 1] == O):
                        neighbors += 1
                    if(list[row + 1][column] == O):
                        neighbors += 1
                    if(list[row + 1][column + 1] == O):
                        neighbors += 1
                elif(column != 0 and column == len(list[row])-1):
                    if(list[row - 1][column - 1] == O):
                        neighbors += 1
                    if(list[row - 1][column] == O):
                        neighbors += 1
                    if(list[row][column - 1] == O):
                        neighbors += 1
                    if(list[row + 1][column - 1] == O):
                        neighbors += 1
                    if(list[row + 1][column] == O):
                        neighbors += 1
            if(row == len(list) -1):
                if(column == 0):
                    if(list[row - 1][column] == O):
                        neighbors += 1
                    if(list[row - 1][column + 1] == O):
                        neighbors += 1
                    if(list[row][column + 1] == O):
                        neighbors += 1
                if(column != 0 and column < len(list[row])-1 ):
                    if(list[row - 1][column - 1] == O):
                        neighbors += 1
                    if(list[row - 1][column] == O):
                        neighbors += 1
                    if(list[row - 1][column + 1] == O):
                        neighbors += 1
                    if(list[row][column - 1] == O):
                        neighbors +=1
                    if(list[row][column + 1] == O):
                        neighbors += 1
                if(column == len(list[row]) -1):
                    if(list[row - 1][column - 1] == O):
                        neighbors += 1
                    if(list[row - 1][column] == O):
                        neighbors += 1
                    if(list[row][column - 1] == O):
                        neighbors += 1
            if(neighbors > 4):
                newboard[row][column] = d
            elif(neighbors == 3):
                newboard[row][column] = O
            elif(neighbors == 2):
                newboard[row][column] = list[row][column]
            elif(neighbors == 4):
                newboard[row][column] = list[row][column]
            else:
                newboard[row][column] = d
            #if(neighbors < 2):
                #newboard[row][column] = d
            #if(neighbors > 4):
                #newboard[row][column] = d
            #if(neighbors == 3):
               # newboard[row][column] = O
            #else:
                #if(list[row][column] == d):
                #    newboard[row][column] = d
                #else:
                  #  newboard[row][column] = O
    return newboard


while True:
    print("would you like to continue this game?")
    answer = input('''answer '5' for five generations 
or answer '10' for ten generations 
or say literally anything else if  you don't want to keep going 
or dial '278' to speak to lindsay in accounting: ''')
    if(answer == "5"):
        for i in range(5):
            print("This is generation " + str(i + 1))
            board = generateBored(board)
            printBoard(board)
            sleep(1.5)
    elif(answer == "10"):
        for i in range(10):
            print("This is generation " + str(i + 1))
            board = generateBored(board)
            printBoard(board)
            sleep(1.49999999)
    elif(answer == "278"):
        lindsay = input('''
        lindsay does not wish to speak to you right now
        leave a message that will be left unheard: ''')
        msg = ""
        for i in range(len(lindsay)):
            if(i % 2 == 0):
                msg += lindsay[i].lower()
            elif(i % 2 == 1):
                msg += lindsay[i].upper() 
        print(msg)  
    else:
        break