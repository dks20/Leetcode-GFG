class Solution:
    def longestPalindrome(self, s: str) -> int:
        countChar = set()
        res = 0

        for i in s:
           if i in countChar:
                res +=2
                countChar.remove(i)
           else:
               countChar.add(i)

        return res + 1 if countChar else res




        for count in countChar.values():
            if count % 2 != 0:
                res += 1
                break




        return res
        