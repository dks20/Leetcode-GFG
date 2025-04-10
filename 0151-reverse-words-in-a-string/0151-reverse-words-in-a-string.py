class Solution:
    def reverseWords(self, s: str) -> str:
        word = s.split()
        rever = word[::-1]
        return " ".join(rever)
        
        