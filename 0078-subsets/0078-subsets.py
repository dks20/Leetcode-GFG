class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        ans = []
        n =len(nums)

        def helper(i,curr):
            if i >= n:
                ans.append(curr[:])
                return
            
            curr.append(nums[i])
            helper(i+1,curr)
            curr.pop()
            helper(i+1,curr)
        helper(0,[])

        return ans
        