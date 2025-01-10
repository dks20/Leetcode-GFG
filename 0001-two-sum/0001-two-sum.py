class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hashm = {}

        for i  in range(len(nums)):
            if target - nums[i] in hashm:
                return [hashm.get(target - nums[i]),i]
            else:
                hashm[nums[i]] = i
            
        
   
             
        