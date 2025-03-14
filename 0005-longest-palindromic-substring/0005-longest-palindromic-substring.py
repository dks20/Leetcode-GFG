class Solution:
    def longestPalindrome(self, s: str) -> str:
        ans = ''
        resLen = 0

        for i in range(len(s)):
            l,r = i,i
            while l>=0 and r < len(s) and s[l] == s[r]:
                if resLen < (r -l +1):
                    resLen = r - l+1
                    ans = s[l:r+1]
                l -= 1
                r += 1
                
            l=i
            r=i+1
            while l>=0 and r< len(s) and s[l]==s[r]:
                if resLen < r-l+1:
                    resLen = r -l +1
                    ans = s[l:r+1]
                l -= 1
                r +=1
        
        return ans
            

        return ans
        