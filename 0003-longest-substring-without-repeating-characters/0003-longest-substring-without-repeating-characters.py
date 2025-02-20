class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:

       ans = 0
       sett = set()
       l = 0

       for i in range(len(s)):
        while s[i] in sett:
            sett.remove(s[l])
            l+=1
        sett.add(s[i])
        ans = max(ans,i-l +1)
        
       return ans
            





       
       
       
       
       
       
       
       
       
       
       
       
       
       
       
       
       
       
       
       
       
       
       
       
       
       
       
       
       
       
       
       
       
       
       
       
       
       
       
       
       
       
       
       
       
       
        # charSet = set()
        # l = 0
        # ans = 0

        # for r in range(len(s)):
        #     while s[r] in charSet:
        #         charSet.remove(s[l])
        #         l+=1
        #     charSet.add(s[r])
        #     ans = max(ans,r-l+1)
        # return ans
            
        