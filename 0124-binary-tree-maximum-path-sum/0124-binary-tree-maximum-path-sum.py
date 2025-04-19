# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:

        def helper(root):
            if not root:
                return 0
            left = helper(root.left)
            right = helper(root.right)

            left = max(left,0)
            right = max(right,0)
            
            currsum = left + right + root.val
            self.ans = max(self.ans,currsum)

            return max(left,right) + root.val

        self.ans = float('-inf')
        helper(root)
        return self.ans

        