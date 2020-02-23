
#---------------------------------------------------------------------------------------------------

def boardGenerator():
    num_of_rows = 10
    num_of_cols = 10
    board = []
    for row in range(num_of_rows):
        boardRow = []
        for col in range(num_of_cols):
            boardRow.append(None)
            board.append(boardRow)
    return board

#---------------------------------------------------------------------------------------------------\

def printBoard(board):
    numRow = len(board)
    numCol = len(board[0])
    #-------------------------------------------------
    # Arrays of string to display in the console
    stringArray = []
    borderstring = "+{}\n".format("---+"*numCol)
    #-------------------------------------------------

    #-------------------------------------------------
    # Top border, which looks like
    # +---+-------+
    stringArray.append(borderstring)
    #-------------------------------------------------

    # Double nested for loop to iterate 2-dimentional array using indexes
    for xIndex in range(numRow):
        #-------------------------------------------------
        # Create left size boarder which looks like
        # |
        stringArray.append("|")
        #-------------------------------------------------

        for yIndex in range(numCol):
            if (board[xIndex][yIndex] == None):
                stringArray.append("{:>3}|".format(""))
        else:
            stringArray.append("{:>3}|".format(board[xIndex][yIndex]))

        #-------------------------------------------------
        # *newline
        stringArray.append("\n")
        # Middle border / Bottom border
        stringArray.append(borderstring)
        #-------------------------------------------------
    print(''.join(stringArray))

def main():

    print("Hello World")
    msg = []

    board = boardGenerator()

    printBoard(board)

if __name__ == "__main__":
    main()