# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        if not root:
            return -1

        count =0
        result = None

        def helper(root):
            nonlocal count,result
            if not root:
                return None
            helper(root.left)
            count= count+1
            if count == k:
                result = root.val
                return 
            helper(root.right)
        helper(root)
        return result
            
            

        