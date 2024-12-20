class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:

        hashmap = {}

        for i in range(len(nums)):
            comp = target - nums[i]

            if(comp in hashmap):
                return [hashmap.get(comp),i]
            
            hashmap[nums[i]] = i
        
        return [-1,-1]
             
        