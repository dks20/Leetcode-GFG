class Solution:
    def romanToInt(self, s: str) -> int:
        hmap = {"I" : 1,
                "V" : 5,
                "X" : 10,
                "L" :50,
                "C" : 100,
                "D" : 500,
                "M" :1000}

        ans = 0

        for i in range(len(s)):
            if i+1 < len(s) and s[i] == "I" and (s[i+1] == "V" or s[i+1] == "X"):
                ans -= hmap[s[i]]
            elif i+1 < len(s) and s[i] == "X" and (s[i+1] == "L" or s[i+1] == "C"):
                ans -= hmap[s[i]]
            elif i+1 < len(s) and s[i] == "C" and (s[i+1] == "D" or s[i+1] == "M"):
                ans -= hmap[s[i]]
            else:  
                ans += hmap[s[i]]

        return ans

        