class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        end = m + n -1
        pt1= m-1
        pt2 = n-1

        if m ==0:
            for i in range(pt2+1):
                nums1[i] = nums2[i]

        while pt2 >=0 and pt1 >= 0 :
            if nums2[pt2] >= nums1[pt1]:
                nums1[end] = nums2[pt2]
                pt2 -= 1
                end -= 1
            else:
                nums1[end] = nums1[pt1]
                pt1 -= 1
                end -= 1
        if pt2 >= 0:
            for i in range(pt2+1):
                nums1[i] = nums2[i]




        

    
        

       