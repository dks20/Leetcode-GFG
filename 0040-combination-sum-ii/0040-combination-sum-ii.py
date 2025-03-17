class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        ans =[]
        candidates.sort()
        n = len(candidates)

        def helper(idx ,arr , total):
            if total == target:
                ans.append(arr[::])
                return
            if idx == n or total > target:
                return


            arr.append(candidates[idx])
            helper(idx+1 , arr , total + candidates[idx])
            arr.pop()

            while idx +1 < n and candidates[idx] == candidates[idx+1]:
                idx+=1
            helper(idx+1 , arr , total)
           

        helper(0,[],0)
        return ans