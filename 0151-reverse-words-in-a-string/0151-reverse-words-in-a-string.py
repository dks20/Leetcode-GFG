class Solution:
    def reverseWords(self, s: str) -> str:
        s = s[::-1]
        ans = ""
        i = 0
        word = ""

        while i < len(s):
            if s[i] != " ":
                word += s[i]
            if (s[i]== " " or i == len(s) -1) and word:
                ans += " " + word[::-1]
                word = ""

            i+=1
        
        return ans[1:len(ans)]








        
        