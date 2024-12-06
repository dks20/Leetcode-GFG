class Solution:
    def majorityElement(self, nums: List[int]) -> int:
       
       freq,ans = 0,0

       for i in range(len(nums)):
        if freq == 0:
            ans = nums[i]
            
        freq += 1 if nums[i] == ans else -1

       return ans

    
        


       

        