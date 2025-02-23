class Solution:
    def findContentChildren(self, g: List[int], s: List[int]) -> int:
        g.sort()
        s.sort()
        co=len(g)
        j=0
        a=0
        for i in s:
            if i>=g[j]:
                j+=1
                a+=1
            if a==co:
                return a
        return a