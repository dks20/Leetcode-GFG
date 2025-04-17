class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
       ans = []
       n = len(intervals)
       intervals.sort(key= lambda x:x[0])
       ans.append(intervals[0])

       for i in range(1,n):
         if intervals[i][0] <= ans[-1][1]:
            ans[-1] = [ans[-1][0], max(ans[-1][1],intervals[i][1])]
         else:
            ans.append(intervals[i])

       return ans

        


        

       



