class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
       
        m = len(matrix)
        n = len(matrix[0])

        top , bot = 0 , m-1

        while top <= bot:
            mid = (bot + top) //2
            if target > matrix[mid][-1]:
                top = mid + 1
            elif target < matrix[mid][0]:
                bot = mid-1
            else:
                break

        row = (bot + top) //2

        l = 0 
        r = n-1

        while l<= r:
            mid = (r+l)//2
            if matrix[row][mid] > target:
                r = mid -1
            elif target > matrix[row][mid]:
                l =mid +1
            else:
                return True

        return False

    
        

       
       
       
       
       
       
       
       
       
       
       
       
       
       
       
       
       
       
       
       
       
       
       
       
       
       
       
       
       
       
       
       
        # m= len(matrix)
        # n = len(matrix[0])

        # for i in range(m):
        #     if target < matrix[i][n-1]:
        #         for nums in matrix[i]:
        #             if nums == target:
        #                 return True
        #         else:
        #             return False
        #     elif target == matrix[i][n-1]:
        #         return True
           
        # return False
    

    
        