class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        board = [["." for i in range(n)] for i in range(n)]
        ans =[]

        def isSafe(row,col):
            for i in range(n):
                if (board[i][col] == "Q"):
                    return False
            
            r = row 
            c = col
            while r >=0 and c >=0:
                if (board[r][c] == "Q"):
                    return False
                r-=1
                c-=1
            
            r,c = row , col
            while r >=0 and c<n:
                if (board[r][c] == "Q"):
                    return False
                r-=1
                c+=1

            return True

        def nQueen(row):
            if row == n:
                ans.append(["".join(row) for row in board])
                return
                

            for col in range(n):
                if(isSafe(row,col)):
                    board[row][col] = "Q"
                    nQueen(row +1)
                    board[row][col] = "."

        nQueen(0)
        return ans


        