class Solution:
    def myAtoi(self, s: str) -> int:
        ans = 0
        n = len(s)
        i = 0
        max_int = (2**31)-1
        min_int = -2**31

        while i < n and s[i] == " ":
            i+=1

        sign = 1
        if i < n and s[i] == "-":
            sign = 0
            i+=1
        elif i <n and s[i] == "+":
            i+=1

        while i <n and s[i].isdigit():
            curr = int(s[i])
            
            
            # ans <= int_max and ans >= int_min
            if ans > (max_int - curr)//10:
               return max_int if sign else min_int 

            ans = (ans * 10) + curr

            
            i+=1 
        
        return ans if sign else -1*ans

        
