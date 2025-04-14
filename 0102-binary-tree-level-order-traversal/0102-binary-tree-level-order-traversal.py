# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
      if not root:
        return []
      que = deque()
      que.append(root)
      ans = []
      

      while que:
        currlevel = []
        for i in range(len(que)):
            currNode = que.popleft()
            currlevel.append(currNode.val)
            if currNode.left:
                que.append(currNode.left)
            if currNode.right:
                que.append(currNode.right)
        ans.append(currlevel)

      return ans



            




