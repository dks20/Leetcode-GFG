class Solution:
    def singleNonDuplicate(self, nums: List[int]) -> int:
        start = 0
        end = len(nums)-1

        if len(nums) == 1:
            return nums[0]        #[1,1,2]
        
    
        while (start < end ):
            mid = start + (end - start)//2

            if nums[mid] != nums[mid-1] and nums[mid ] != nums[mid +1]:
                return nums[mid]

            if (mid%2 ==0) :
                if nums[mid] == nums[mid +1]:
                    start = mid +2
                else:
                    end = mid -2
            else:
                if nums[mid] == nums[mid +1]:
                   end = mid -1
                else:
                    start = mid+1

        return nums[start]

            

        
       
        