n=int(input())
board=[list(map(int, input().split())) for _ in range(n)]

class Move:
    
    def Left(board):
        moved_board=[0 for _ in range(n)]
        for i in range(n):
            moved_board[i]=board[i][1:]
            moved_board[i].insert(n-1, 0)
            moved_board[i][0]=moved_board[i][0]+board[i][0]
        return moved_board
    
    def Right(board):
        moved_board=[0 for _ in range(n)]
        for i in range(n):
            moved_board[i]=board[i][:n-1]
            moved_board[i].insert(0, 0)
            moved_board[i][n-1]=moved_board[i][n-1]+board[i][n-1]
        return moved_board
    
    def Up(board):
        moved_board=[[0]*n for _ in range(n)]
        for j in range(n):
            for i in range(n-1):
                moved_board[i][j]=board[i+1][j]
            moved_board[n-1][j]=0
            moved_board[0][j]=moved_board[0][j]+board[0][j]
        return moved_board
    
    def Down(board):
        moved_board=[[0]*n for _ in range(n)]
        for j in range(n):
            for i in range(1, n):
                moved_board[i][j]=board[i-1][j]
            moved_board[0][j]=0
            moved_board[n-1][j]=moved_board[n-1][j]+board[n-1][j]
        return moved_board
    
moved=Move.Down(board)
for i in range(n):
    print(moved[i])