class Solution:
    def countPrimes(self, n: int) -> int:

        if n <= 2:
         return 0

        tempArr = [1]* n
        tempArr[0] = tempArr[1] = 0
        ans = 0

        for i in range(1,int(n**0.5) + 1):
            if tempArr[i] == 1:  # If i is a prime number
             for j in range(i*i, n, i):
                tempArr[j] = 0 
        
        ans = sum(tempArr)
        return ans







        