class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:

        ans = []
        def helper(idx , arr):
            if sum(arr) == target:
                ans.append(arr[::])
                return
            if sum(arr) > target or idx >= len(candidates):
                return

            arr.append(candidates[idx])
            helper(idx,arr)
            arr.pop()
            helper(idx+1,arr)

        helper(0,[])

        return ans
        