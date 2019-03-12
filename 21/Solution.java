/**
 * Definition for singly-linked list.
 * public class ListNode {
 *     int val;
 *     ListNode next;
 *     ListNode(int x) { val = x; }
 * }
 */
class Solution {
    public class ListNode {
        int val;
        ListNode next;
        ListNode(int x) {
            val = x;
        }
    }
    public ListNode mergeTwoLists(ListNode l1, ListNode l2) {
        ListNode l = new ListNode(null);
        while (l1.next != null && l2.next != null) {
            if (l1.val < l2.val) {
                l.next = new ListNode(l1.val);
                l1 = l1.next;
            } else {
                l.next = new ListNode(l2.val);
                l2 = l2.next;
            }
            l = l.next;
        }
        return l.next;
    }
}