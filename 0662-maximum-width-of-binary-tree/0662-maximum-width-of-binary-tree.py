# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def widthOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        ans = 0
        if not root:
            return ans
        
        queue = deque([(root,1,0)])

        while queue:
            lev = []
            for i in range(len(queue)):
                node,cur_num, cur_level = queue.popleft()
                lev.append(cur_num)
                if node.left:
                    queue.append((node.left,cur_num*2,cur_level+1))
                if node.right:
                    queue.append((node.right,cur_num*2+1,cur_level+1))
                
            ans = max(ans, lev[-1] - lev[0] +1)

        return ans

        