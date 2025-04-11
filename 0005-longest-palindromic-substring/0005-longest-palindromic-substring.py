class Solution:
    def longestPalindrome(self, s: str) -> str:
       n = len(s)
       long = 0
       ans = ""

       for i in range(n):
            l,r = i,i
            while(l >= 0 and r < n and s[l] == s[r]):
                curr_long = r -l +1
                if curr_long > long:
                    ans = s[l:r+1]
                    long = curr_long 
                l -=1
                r +=1

            l,r = i,i+1
            while(l>=0 and r < n and s[l] == s[r]):
                if long < (r-l+1):
                    long = r -l +1
                    ans = s[l:r+1]
                r+=1
                l-=1

       return ans
        