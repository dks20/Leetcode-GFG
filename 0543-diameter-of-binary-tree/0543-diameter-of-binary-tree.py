# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        self.ans = 0
        def helper(root):
            if not root:
                return 0

            left = helper(root.left)
            right = helper(root.right)
            
            self.ans  = max(self.ans  , (left + right))
            return max(left , right) + 1
        helper(root)

        return self.ans 

        #    if not root:
    #     return 0

    #    left = self.diameterOfBinaryTree(root.left)
    #    right = self.diameterOfBinaryTree(root.right)

    #    max(left , right) + 1

    #    ans =  max(ans, left + right)
