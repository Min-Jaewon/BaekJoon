n=int(input())
board=[list(map(int, input().split())) for _ in range(n)]

def is_exp(n):
    return (n&(n-1))==0
    
class Move:
    def Left(board):
        moved_board=[[0]*n for _ in range(n)]
        for i in range(n):
            j_=0
            for j in range(n):
                if board[i][j]!=0:
                    moved_board[i][j_]=board[i][j]
                    j_+=1
            for j in range(n-1):
                if is_exp(moved_board[i][j]+moved_board[i][j+1]):
                    moved_board[i][j]=moved_board[i][j]+moved_board[i][j+1]
                    for k in range(j+1, n-1):
                        moved_board[i][k]=moved_board[i][k+1]
                    moved_board[i][n-1]=0
        return moved_board
    
    def Right(board):
        moved_board=[[0]*n for _ in range(n)]
        for i in range(n):
            j_=n-1
            for j in reversed(range(n)):
                if board[i][j]!=0:
                    moved_board[i][j_]=board[i][j]
                    j_-=1
            for j in range(n-1, 0, -1):
                if is_exp(moved_board[i][j]+moved_board[i][j-1]):
                    moved_board[i][j]=moved_board[i][j]+moved_board[i][j-1]
                    for k in range(j-1, 0,-1):
                        moved_board[i][k]=moved_board[i][k-1]
                    moved_board[i][0]=0
        return moved_board
    
    def Up(board):
        moved_board=[[0]*n for _ in range(n)]
        for j in range(n):
            i_=0
            for i in range(n):
                if board[i][j]!=0:
                    moved_board[i_][j]=board[i][j]
                    i_+=1
            for i in range(n-1):
                if is_exp(moved_board[i][j]+moved_board[i+1][j]):
                    moved_board[i][j]=moved_board[i][j]+moved_board[i+1][j]
                    for k in range(i+1, n-1):
                        moved_board[k][j]=moved_board[k+1][j]
                    moved_board[n-1][j]=0
        return moved_board
    
    def Down(board):
        moved_board=[[0]*n for _ in range(n)]
        for j in range(n):
            i_=n-1
            for i in reversed(range(n)):
                if board[i][j]!=0:
                    moved_board[i_][j]=board[i][j]
                    i_-=1
            for i in range(n-1, 0 ,-1):
                if is_exp(moved_board[i][j]+moved_board[i-1][j]):
                    moved_board[i][j]=moved_board[i][j]+moved_board[i-1][j]
                    for k in range(i-1, 0, -1):
                        moved_board[k][j]=moved_board[k-1][j]
                    moved_board[0][j]=0
        return moved_board
    
def findMax(board):
    maxvalue=0
    for i in range(n):
        for j in range(n):
            if board[i][j]>maxvalue:
                maxvalue=board[i][j]
    return maxvalue


def DFS(board, cnt):
    if cnt==5:
        return findMax(board)
    r_board=Move.Right(board)
    l_board=Move.Left(board)
    u_board=Move.Up(board)
    d_board=Move.Down(board)
    
    r_max=DFS(r_board, cnt+1)
    l_max=DFS(l_board, cnt+1)
    u_max=DFS(u_board, cnt+1)
    d_max=DFS(d_board, cnt+1)
    
    return max(r_max, l_max, u_max, d_max)


print(DFS(board, 0))
   