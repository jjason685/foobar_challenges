def answer(src, dest):
    board = [[0 for i in range(10)] for j in range(10)]
    fillBoard(board, src, 0)
    if src == dest:
        return 0
    return board[(int) (dest/8)][(int) (dest%8)]

def fillBoard(board, currentPos, numOfMoves):
    currentx = currentPos/8
    currenty = currentPos%8
    
    possibleRes = [1,2,2,1,2,-1,1,-2,-1,-2,-2,-1,-2,1,-1,2]
    
    for i in range(0, 16, 2):
        newx = currentx + possibleRes[i]
        newy = currenty + possibleRes[i+1]
        if newx >= 0 and newy >= 0 and newx < 8 and newy < 8:
            if board[newx][newy] == 0 or board[newx][newy] > numOfMoves+1:
                board[newx][newy] = numOfMoves+1
                fillBoard(board, newx * 8 + newy, numOfMoves+1)

#print(answer(19,36)) test case
#print(answer(0,1)) test case
#print(answer(0,9)) test case

"""
code fully working, not brute forcing (recursion would take too long) but instead finding the distance to each point
on the board by pointing in 2d arr
"""
