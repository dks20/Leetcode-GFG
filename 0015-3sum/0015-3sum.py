class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
       nums.sort()
       ans = []
       #[-4,-1,-1,0,1,2]
       for i  in range(len(nums)):
         if i > 0 and nums[i] == nums[i-1]:
            continue
         l = i+1
         r = len(nums) -1

         while l < r:
            currSum = nums[i] + nums[l] + nums[r]
            if currSum == 0:
                ans.append([nums[i],nums[l],nums[r]])
                l+=1
                while l < r and nums[l] == nums[l-1]:
                    l+=1
                r-=1
                while l< r and nums[r] == nums[r+1]:   
                   r-=1
                
            elif currSum > 0:
                r-=1
                while l< r and nums[r] == nums[r+1]:   
                   r-=1
            else:
                l +=1
                while l < r and nums[l] == nums[l-1]:
                    l+=1
       
       return ans
 

        