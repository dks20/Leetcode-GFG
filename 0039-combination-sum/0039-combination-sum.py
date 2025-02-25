class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:

        ans = []
        def helper(idx , arr,total):
            if total == target:
                ans.append(arr[::])
                return
            if total > target or idx >= len(candidates):
                return

            arr.append(candidates[idx])
            helper(idx,arr, total + candidates[idx])
            arr.pop()
            helper(idx+1,arr,total)

        helper(0,[],0)

        return ans
        