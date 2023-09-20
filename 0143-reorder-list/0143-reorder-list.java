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
    public void reorderList(ListNode head) {
        if(head == null || head.next == null){
            return;
        }

        ListNode fh  = head;
        ListNode mid = Findmid(head);
        ListNode sh = reverse(mid);

        while(fh != null && sh != null){
            ListNode temp = fh.next;
            fh.next = sh;
            fh = temp;

            temp = sh.next;
            sh.next = fh;
            sh = temp;

        }
        if(fh != null){
            fh.next = null;
        }
        
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
        if(mid == null || mid.next == null){
            return mid;

        }

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