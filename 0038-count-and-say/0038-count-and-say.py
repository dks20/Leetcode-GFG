class Solution:
    def countAndSay(self, n: int) -> str:
        ans = ""
        def helper(n):  #2
             if n == 1:
                return "1"
            
             prev = helper(n-1)
             count = 1
             ans = ""
             y = len(prev)
             
             for i in range(1,y):
                if prev[i] == prev[i-1]:
                    count +=1
                else:
                    ans += str(count) + str(prev[i-1])
                    count =1
             ans += str(count) + str(prev[-1])
             return ans
        
        return helper(n)


            


             




        