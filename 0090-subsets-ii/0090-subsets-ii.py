class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        ans  = []
        nums.sort()
        n = len(nums)

        def helper(idx , arr):
            if idx == n:
                ans.append(arr[:])
                return
            arr.append(nums[idx])
            helper(idx+1,arr)
            arr.pop()
            while idx +1 < n and nums[idx] == nums[idx+1]:
                idx +=1 
            helper(idx+1,arr)

        helper(0,[])
        return ans
        