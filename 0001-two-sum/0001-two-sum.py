class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hashMap = {}

        for i in range(len(nums)):
            value = target - nums[i]
            if value in hashMap:
                return [i, hashMap.get(value)]
            else:
                hashMap[nums[i]] = i
        return [-1,-1]