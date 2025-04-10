class Solution:
    def reverseWords(self, s: str) -> str:
        # Step 1: Clean up the input
        def trim_spaces(s):
            res = []
            i = 0
            while i < len(s):
                if s[i] != ' ':
                    res.append(s[i])
                elif res and res[-1] != ' ':
                    res.append(' ')
                i += 1
            if res and res[-1] == ' ':
                res.pop()
            return res

        # Step 2: Reverse characters in range
        def reverse(l, left, right):
            while left < right:
                l[left], l[right] = l[right], l[left]
                left += 1
                right -= 1

        # Step 3: Reverse each word
        def reverse_each_word(l):
            n = len(l)
            start = 0
            for i in range(n + 1):
                if i == n or l[i] == ' ':
                    reverse(l, start, i - 1)
                    start = i + 1

    # Apply steps
        l = trim_spaces(s)
        reverse(l, 0, len(l) - 1)
        reverse_each_word(l)
        return ''.join(l)







        
        