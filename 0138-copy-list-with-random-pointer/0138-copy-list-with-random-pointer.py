"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':

        oldToCopy = {None : None}

        curr =  head
        while curr:
            newNode = Node(curr.val)
            oldToCopy[curr] = newNode
            curr = curr.next

        curr = head
        
        copyHead  = oldToCopy[head]

        while curr:
            copyHead.next = oldToCopy[curr.next]
            copyHead.random = oldToCopy[curr.random]
            curr = curr.next
            copyHead = copyHead.next

        return oldToCopy[head]
            