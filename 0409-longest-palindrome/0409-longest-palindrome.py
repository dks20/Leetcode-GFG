class Solution:
    def longestPalindrome(self, s: str) -> int:
        countChar = defaultdict(int)
        res = 0

        for i in s:
            countChar[i] += 1
            if  countChar[i] % 2 ==0 :
                res +=2
        
        for count in countChar.values():
            if count % 2 != 0:
                res += 1
                break




        return res
        