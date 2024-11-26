class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        # optimized
        r = []
        c = []
        row = len(matrix)
        col = len(matrix[0])

        for i in range(row):
            for j in range(col):
                if matrix[i][j] == 0:
                    r.append(i)
                    c.append(j)

        for i in range(row):
            for j in range(col):
                if i in r or j in c:
                    matrix[i][j] = 0

                


        
       

        

        

       

        