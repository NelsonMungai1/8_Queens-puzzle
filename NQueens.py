N=8
def solveNQuens(board,col):
    if col==N:
        print(board)
        return True
    for i in range(N):
        if isSafe(board,i,col):
            board[i][col]=1
            if solveNQuens(board,col+1):
                return True
            board[i][col]=0
    return False

def isSafe(board,row,col):
    for x in range(col):
        if board[row][x]==1:
            return False
    for x,y in zip(range(row,-1,-1),range(col,-1,-1)):
        if board[x][y]==1:
            return False
    for x,y in zip(range(row,N,1),range(col,-1,-1)):
        if board[x][y]==1:
            return False
    return True

board=[[0 for x in range(N)]for y in range(N)]
if not solveNQuens(board,0):
    print("No solution found")

if __name__=="__main__":
    solveNQuens(board,0)
