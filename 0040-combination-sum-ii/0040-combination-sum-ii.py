class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        ans =[]
        candidates.sort()

        def helper(idx ,arr , total):
            if total == target:
                ans.append(arr[:])
                return
            if idx >= len(candidates) or total > target:
                return

            arr.append(candidates[idx])
            helper(idx +1,arr,total + candidates[idx])
            arr.pop()

            while idx+1 < len(candidates) and candidates[idx] == candidates[idx+1]:
                idx+=1
            helper(idx+1,arr,total)

        helper(0,[],0)
        return ans