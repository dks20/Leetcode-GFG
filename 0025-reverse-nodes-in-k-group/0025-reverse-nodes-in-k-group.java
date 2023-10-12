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
    public ListNode reverseKGroup(ListNode head, int k) {
        int length = len(head);
        return reverseLL(head,k,length);

    }
    public int len(ListNode head){
        int leng = 0;
        ListNode temp = head;
        while(temp != null){
            temp = temp.next ;
            leng++; 
        }
        return leng;

    }
    public ListNode reverseLL(ListNode head, int k,int length){
        if(length < k){
            return head;
        }

        ListNode prev = null;
        ListNode curr = head;
        int count = 0;

        while(curr != null && count<k){
            ListNode nex = curr.next;
            curr.next = prev;
            prev = curr;
            curr = nex;
            count++;
        }
        if(curr != null){
            head.next = reverseLL(curr,k,length -k);
        }
        return prev;
    }
}