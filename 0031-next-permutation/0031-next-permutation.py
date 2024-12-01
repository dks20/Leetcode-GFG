class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        pvt =-1

        for i in range(len(nums)-2,-1,-1):
            if nums[i] < nums[i+1]:
                pvt = i
                break
        
        if pvt == -1:
            nums.reverse()
        else:
            for j in range(len(nums)-1,pvt,-1):
                if nums[pvt]< nums[j]:
                    nums[pvt],nums[j] = nums[j],nums[pvt]
                    break
            nums[pvt + 1:] = reversed(nums[pvt + 1:])


        