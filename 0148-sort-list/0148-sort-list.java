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
    public ListNode sortList(ListNode head) {

        if(head == null ||  head.next == null){
            return head;
        }
        ListNode  s = head;
        ListNode  f = head;
        ListNode  temp = null;

        while(f != null && f.next != null){
            temp = s;
            s= s.next;
            f = f.next.next;
        }

        temp.next = null;
        ListNode mid = s;

        ListNode L1 = sortList(head);
        ListNode L2 = sortList(mid);

        ListNode ans = merge(L1,L2);
        
        return ans;
        
    }

    ListNode merge(ListNode L1, ListNode L2){
        ListNode result = new ListNode(0);
        ListNode temp = result;
        ListNode p1 = L1 ;
        ListNode p2 = L2 ;

        while(p1 != null && p2 != null){
            if(p1.val <= p2.val){
                temp.next = p1;
                p1 = p1.next;
            }else{
                temp.next = p2;
                p2 = p2.next;    
            }
            temp = temp.next;
        }
        while(p1 != null){
            temp.next = p1;
            p1 = p1.next;
            temp = temp.next;
        }
        while(p2 != null){
            temp.next = p2;
            p2 = p2.next;
            temp = temp.next;
        }
        return result.next;
    }
}