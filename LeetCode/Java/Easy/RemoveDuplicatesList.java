/* 83. Remove Duplicates from Sorted List
Given a sorted linked list, delete all duplicates such that each element appear only once.

Example 1:

Input: 1->1->2
Output: 1->2
Example 2:

Input: 1->1->2->3->3
Output: 1->2->3
*/

/**
 * Definition for singly-linked list.
 * public class ListNode {
 *     int val;
 *     ListNode next;
 *     ListNode(int x) { val = x; }
 * }
 */
class Solution {
    public ListNode deleteDuplicates(ListNode head) {
        if (head == null) return null;
        head.next = deleteHelp(head, head.next);
        return head;
    }
    public ListNode deleteHelp(ListNode h1, ListNode n1) {
        if (n1 == null) return null;
        if (h1.val == n1.val) {
            h1.next = deleteHelp(h1, n1.next);
        } else if (n1.next == null) {
            return n1;
        } else {
            h1.next = n1;
            n1.next = deleteHelp(n1, n1.next);
        }
        return h1.next;
    }
}