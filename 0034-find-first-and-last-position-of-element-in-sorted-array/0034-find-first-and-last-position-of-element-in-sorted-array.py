class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        s =0
        e = len(nums)-1

        while(s <= e):
            mid = (s + e)//2

            if nums[mid] > target :
                e = mid -1
            if nums[mid] < target:
                s = mid + 1

            if nums[mid] == target:
                s = mid
                e = mid
                while s > 0 and nums[s-1] == nums[mid]:
                    s -= 1
                while e < len(nums)-1 and nums[e+1] == nums[mid]:
                    e += 1
                return [s,e]

        return [-1,-1]
                
                

        