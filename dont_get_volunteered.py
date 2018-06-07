def answer(src, dest):
    board = [[0 for i in range(8)] for j in range(8)]
    fillBoard(board, src, 0)
    if src == dest:
        return 0
    return board[(int) (dest/8)][(int) (dest%8)]

def fillBoard(board, currentPos, numOfMoves):
    currentx = currentPos/8
    currenty = currentPos%8
    
    possibleRes = [1,2,2,1,2,-1,1,-2,-1,-2,-2,-1,-2,1,-1,2]
    
    i = 0
    while i < 16:
        newx = currentx + possibleRes[i]
        newy = currenty + possibleRes[i+1]
        if newx >= 0 and newy >= 0 and newx < 8 and newy < 8:
            if board[newx][newy] == 0 or board[newx][newy] > numOfMoves+1:
                board[newx][newy] = numOfMoves+1
                fillBoard(board, newx * 8 + newy, numOfMoves+1)
        i+=2
