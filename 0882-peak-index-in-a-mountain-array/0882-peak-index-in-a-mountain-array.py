class Solution:
    def peakIndexInMountainArray(self, arr: List[int]) -> int:

        s =0 
        e = len(arr)-1

        while(s < e):
            mid = (s + e)//2

            if mid < len(arr) and arr[mid] > arr[mid+1]:
                e = mid
            else:
                s = mid +1

        return s
        