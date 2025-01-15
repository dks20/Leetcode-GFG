class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        n = len(nums)
        ans = []
        if n < 3 :
            return []
        nums.sort()

        #[-4,-1,-1,0,1,2]

        for i in range(n-2):
            fixval  = nums[i]
            if i > 0 and fixval == nums[i-1]:
                continue
            p1 = i+1
            p2 = n-1
            while p1<p2 :
                if (nums[p1] + nums[p2] + fixval) > 0:
                    p2 = p2-1
                elif (nums[p1] + nums[p2] + fixval) < 0:
                    p1 = p1 + 1
                else:
                    ans.append([fixval , nums[p1] , nums[p2]])
                    p1 += 1
                    while nums[p1] == nums[p1 -1] and p1 < p2:
                        p1 +=1

        return ans


        