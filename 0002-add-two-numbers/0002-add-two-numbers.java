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
    public ListNode addTwoNumbers(ListNode L1, ListNode L2) {
        ListNode ans = new ListNode(0);
        ListNode temp = ans;
        int sum = 0;
        int c = 0;

        while(L1 != null || L2 != null){
            int x = (L1 != null) ? L1.val : 0 ;
            int y = (L2 != null) ? L2.val : 0 ;

            sum = c +x+y;
            c = sum/10;
            sum %= 10;

            temp.next =new ListNode(sum);
            temp = temp.next;
            if(L1 != null){
                L1 = L1.next;
            }
            if(L2 != null){
                L2 = L2.next;
            }
        }
        if(c>0){
            temp.next= new ListNode(1);
        }

        return ans.next;
    }
}