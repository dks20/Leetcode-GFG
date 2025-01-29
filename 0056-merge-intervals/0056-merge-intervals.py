class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        n = len(intervals)
        intervals.sort(key = lambda x:x[0])

        ans = []
        ans.append(intervals[0])

        for i in range(1,n):
            if intervals[i][0] <= ans[-1][1]:
                ans[-1] = [ans[-1][0], max(intervals[i][1], ans[-1][1])]
            else:
                ans.append(intervals[i])

        return ans
        

           

             
        return ans
            

       



