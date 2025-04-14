# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        ans = []
        if not root:
            return ans

        queue = deque([root])
        reverse = False

        while queue:
            level = []
            for i in range(len(queue)):
                curr= queue.popleft()
                level.append(curr.val)
                if curr.left:
                    queue.append(curr.left)
                if curr.right:
                    queue.append(curr.right)     

            if reverse:
                level = level[::-1]
            reverse = not reverse
            ans.append(level)

        return ans