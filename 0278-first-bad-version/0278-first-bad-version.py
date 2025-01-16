# The isBadVersion API is already defined for you.
# def isBadVersion(version: int) -> bool:

class Solution:
    def firstBadVersion(self, n: int) -> int:
        res = n
        l, r = 1, res

        while l <= r:
            m = (l + r) // 2
            if isBadVersion(m):
                res = m  # Update result to current middle
                r = m - 1  # Narrow search to the left half
            else:
                l = m + 1  # Narrow search to the right half

        return res
        