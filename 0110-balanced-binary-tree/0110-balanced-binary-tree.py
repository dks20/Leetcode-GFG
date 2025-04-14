# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        self.ans = 1
        def helper(root):
            if not root:
                return 0

            left = helper(root.left)
            right = helper(root.right)

            height = abs(left -right)
            if height > 1:
                self.ans = 0
            
            return  max(left , right) +1
        helper(root)
        return True if self.ans else False 
        