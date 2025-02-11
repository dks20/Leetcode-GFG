class Solution:
    def myPow(self, x: float, n: int) -> float:
       binary = abs(n)
       ans = 1

       while(binary > 0):
        if binary %2 == 1:
            ans *= x
        x *= x
        binary //= 2

       return ans if n >= 0 else 1 / ans

       #(2 ,5)     * (2,5)
       (2,2) 
       (2,1)
    
