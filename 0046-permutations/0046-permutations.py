class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        ans = []
        n =len(nums)

        def helper(nums,idx):
            if idx >= n:
                ans.append(nums[:])
                return
            
            for i in range(idx,n):

               nums[idx], nums[i] = nums[i] ,nums[idx]
               helper(nums,idx+1)
               nums[idx], nums[i] = nums[i] ,nums[idx]

        helper(nums,0)
        return ans
        