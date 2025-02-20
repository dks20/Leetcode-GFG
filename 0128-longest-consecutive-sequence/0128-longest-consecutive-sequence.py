class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        ans = 0

        nums_set =  set(nums)

        for  i in nums_set:
            if i-1 not in nums_set:
                count = 1
                curr = i
                while curr +1 in nums_set:
                    count +=1
                    curr = curr + 1
                ans = max(count, ans)



        return ans