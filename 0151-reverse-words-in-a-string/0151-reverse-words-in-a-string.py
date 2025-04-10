class Solution:
    def reverseWords(self, s: str) -> str:
        s = [i.strip() for i in s.split()]
        return ' '.join(list(reversed(s)))
        
        