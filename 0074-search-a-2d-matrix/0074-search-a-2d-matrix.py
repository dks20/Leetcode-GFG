class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
       
    #    m = len(matrix)
    #    n = len(matrix[0])

    #    for i  in range(m):
    #     if target > matrix[i][n-1]:
    #         continue
    #     elif target == matrix[i][n-1]:
    #         return True
    #     elif target < matrix[i][n-1]:
    #         start = i
    #         end = n-1

    #         return self.binarySearch(matrix[i],0,m-1,target)

    #     else:
    #         return False
       
    # def binarySearch(self,arr,start,end,target):
    #     while start <= end:
    #         mid = start + (end -start)//2 
    #         if arr[mid] ==  target:
    #             return True
    #         if target < arr[mid]:
    #             return self.binarySearch(arr,start,mid,target)
    #         else:
    #             return self.binarySearch(arr,mid+1,end,target)
    #     return False
        

       
       
       
       
       
       
       
       
       
       
       
       
       
       
       
       
       
       
       
       
       
       
       
       
       
       
       
       
       
       
       
       
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
    

    
        