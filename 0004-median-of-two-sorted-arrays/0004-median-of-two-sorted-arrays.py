class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        m = nums1
        n = nums2

        total = len(m) + len(n)
        half = total//2

        if len(m) > len(n):
            m,n=n,m

        l = 0 
        r = len(m) -1
        while(True):
            mid1 = (l+r)//2
            mid2 = half - mid1 - 2

            mleft = m[mid1] if mid1 >= 0 else float('-inf') 
            mright = m[mid1+1] if mid1+1 < len(m) else float('inf')
            nleft = n[mid2]  if mid2 >= 0 else float('-inf') 
            nright = n[mid2 +1] if mid2+1 < len(n) else float('inf')
            
            if mleft <= nright and nleft <= mright:
                if total %2 ==1:
                    return min(mright,nright)
                else:
                    return (max(mleft,nleft) + min(mright,nright)) /2

            elif mleft > nright :
                r = mid1-1
            else:
                l = mid1+1


        



