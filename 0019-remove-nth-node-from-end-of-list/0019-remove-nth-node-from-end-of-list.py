# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        if not head.next:
            return head.next     #[1,2]  2 ,1
        curr= head
        list_len = 0

        while curr:
            list_len +=1
            curr = curr.next

        curr= head
        prev = None
        n = list_len -n+1  #1
        counter = 1

        while counter < n:
            prev = curr
            curr = curr.next
            counter +=1
        if prev:
            prev.next = curr.next
        else:
            head = head.next
        return head






        