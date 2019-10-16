/* 2. Add Two Numbers
You are given two non-empty linked lists representing two non-negative integers. The digits are stored in reverse order and each of their nodes contain a single digit. Add the two numbers and return it as a linked list.

You may assume the two numbers do not contain any leading zero, except the number 0 itself.

Example:

Input: (2 -> 4 -> 3) + (5 -> 6 -> 4)
Output: 7 -> 0 -> 8
Explanation: 342 + 465 = 807.
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
    public ListNode addTwoNumbers(ListNode l1, ListNode l2) {
        const int TEN = 10;

        ListNode curr1 = l1;
        ListNode curr2 = l2;
        int carry = l1.val + l2.val;
        ListNode result = new ListNode(carry%10);
        carry /= TEN;
        ListNode curr_res = result;
        while (curr1.next != null || curr2.next != null) {
            if (curr1.next != null) {
                carry += curr1.next.val;
                curr1 = curr1.next;
            }
            if (curr2.next != null) {
                carry += curr2.next.val;
                curr2 = curr2.next;
            }
            curr_res.next = new ListNode(carry%TEN);
            carry /= TEN;
            curr_res = curr_res.next;
        }
        if (carry != 0) curr_res.next = new ListNode(carry%TEN);
        return result;
    }
}