/**
 * Definition for singly-linked list.
 * public class ListNode {
 *     int val;
 *     ListNode next;
 *     ListNode() {}
 *     ListNode(int val) { this.val = val; }
 *     ListNode(int val, ListNode next) { this.val = val; this.next = next; }
 * }
 */
class Solution {
    public boolean isPalindrome(ListNode head) {
        ListNode midNode = Findmid(head);
        ListNode secondHead = reverse(midNode);
        ListNode reverseList = secondHead;

        ListNode L1 = head;
        ListNode L2 = secondHead;
    
        while(L1 != null && L2 != null){
            if(L1.val != L2.val){
                break;
            }
            L1 = L1.next;
            L2 = L2.next; 
        }

        reverse(reverseList);

        return L1 ==null || L2 == null ;
    }
    public ListNode Findmid(ListNode head){
        ListNode s = head;
        ListNode f = head;

        while(f != null && f.next != null){
            s = s.next;
            f= f.next.next;
        }

        return s;
    }

    public ListNode reverse(ListNode mid){
        ListNode prev = null;
        ListNode curr = mid;

        while(curr != null){
            ListNode nex = curr.next;
            curr.next = prev;
            prev = curr;
            curr = nex;
        }
        return prev;
    }
}