class Solution:
    def scoreOfString(self, s: str) -> int:
        n = len(s)
        if len(s) ==1:
            return ord(s)
        if n == 0:
            return 0
        p = 0
        ans = 0
        while p < len(s)-1:
            ans += abs(ord(s[p]) - ord(s[p+1]))
            p+=1

        return ans

        
        