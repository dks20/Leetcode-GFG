# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def verticalTraversal(self, root: Optional[TreeNode]) -> List[List[int]]:
        hd_map =defaultdict(list)
        if not root:
            return []

        queue = deque([(root,0,0)])
        while queue:
            node, hd, level = queue.popleft()
            hd_map[hd].append((level,node.val))

            if node.left:
                queue.append((node.left,hd-1,level +1))
            if node.right:
                queue.append((node.right,hd+1,level +1))
        
        ans = []

        for key in sorted(hd_map.keys()):
            level_sorted = sorted(hd_map[key])
            ans.append([val for level,val in level_sorted])
        return ans

            
        