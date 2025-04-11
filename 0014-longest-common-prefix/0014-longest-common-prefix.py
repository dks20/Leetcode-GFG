class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        prefix = ""
        for chars in zip(*strs):  # zip groups ith char from all strings
            if len(set(chars)) == 1:  # all same?
                prefix += chars[0]
            else:
                break
        return prefix