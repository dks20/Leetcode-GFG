class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        m= len(matrix)
        n = len(matrix[0])

        for i in range(m):
            if target < matrix[i][n-1]:
                for nums in matrix[i]:
                    if nums == target:
                        return True
                else:
                    return False
            elif target == matrix[i][n-1]:
                return True
           
        return False
    

    
        