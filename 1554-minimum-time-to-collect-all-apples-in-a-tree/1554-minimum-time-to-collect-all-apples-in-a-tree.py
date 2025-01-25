class Solution:
    def minTime(self, n: int, edges: List[List[int]], hasApple: List[bool]) -> int:

        adj = defaultdict(list)
        for v,u in edges:
           
            adj[v].append(u)
            adj[u].append(v)
        
        #{0:[1,2], 1:[0,4,5], 2:[0,3,6], 3:[2] , 4:[1], 5:[1] , 6:[2]}

        def dfs(curr, parent):
            time = 0

            for i in adj[curr]:
              if i != parent:
                
                time += dfs(i,curr)

            if time or hasApple[curr]:
                return time + 2

            return time

        return max(dfs(0,-1)-2, 0)

                
            

        
        