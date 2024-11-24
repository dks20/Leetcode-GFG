class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        start = 0
        curr = 0
        end = len(nums ) -1

        while curr <= end:
            if nums[curr] == 0:
                temp = nums[start]
                nums[start] = nums[curr]
                nums[curr] = temp
                start = start +1
                curr  = curr +1
            elif nums[curr] == 1 :
                curr = curr +1
            else:
                
                temp = nums[end]
                nums[end] = nums[curr]
                nums[curr] = temp
                end = end -1 
            
