# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:

        def helper(root):
            if not root:
                return 0
            
            leftheight = helper(root.left) 
            rightheight = helper(root.right)

            return max(leftheight , rightheight) +1

        return helper(root)
      
        