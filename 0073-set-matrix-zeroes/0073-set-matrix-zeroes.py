class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        m = len(matrix)
        n = len(matrix[0])

        row = [0] * m #[0,1,0]
        col = [0] * n

        for i in range(m):
            for j in range(n):
                if matrix[i][j] == 0:
                    row[i] = 1
                    col[j] = 1
        
        for i in range(m):
            if row[i]:
                for j in range(n):
                    matrix[i][j] = 0

        for i in range(n):
            if col[i]:
                for j in range(m):
                    matrix[j][i] = 0

        


                


        
       

        

        

       

        