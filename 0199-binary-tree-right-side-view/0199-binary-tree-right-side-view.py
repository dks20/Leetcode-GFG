# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        ans = []

        def helper(level , root):
            if not root:
                return

            if level == len(ans):
                ans.append(root.val)

            helper(level+1 , root.right)
            helper(level+1 , root.left)

        helper(0,root)
        return ans

            