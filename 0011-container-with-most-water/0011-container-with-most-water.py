class Solution:
    def maxArea(self, height: List[int]) -> int:
       maxa = 0
       l = 0
       r = len(height)-1

       while (l<r):
        area = (r-l) * min(height[r],height[l])
        maxa = max(maxa , area)
        if height[l] < height[r]:
            l +=1
        else:
            r -= 1
            

       return maxa
        