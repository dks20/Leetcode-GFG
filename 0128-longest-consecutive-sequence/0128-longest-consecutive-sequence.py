class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        ans = 0

        nums_set = set(nums)

        for i in nums_set:
            if i -1 not in nums_set:
                curr = i
                count = 1
                while curr +1 in nums_set:
                    count += 1
                    curr +=1
                ans = max(ans , count)

        return ans

