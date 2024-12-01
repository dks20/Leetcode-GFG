class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        last = m +n -1
        mindex = m-1
        nindex = n-1

        if m ==0:
            for i in range(n):
                nums1[i] = nums2[i]
        

        while (mindex >= 0  and nindex >= 0):
            if (nums1[mindex] >= nums2[nindex]):
                nums1[last] = nums1[mindex]
                mindex -= 1
                last -=1
            else:
                nums1[last] = nums2[nindex]
                nindex -= 1
                last -=1

        while nindex >=0:
            nums1[last] = nums2[nindex]
            nindex -= 1
            last -=1

        