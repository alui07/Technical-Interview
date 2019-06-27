import java.util.*;
import java.lang.*;

public class MergeLists extends ListNode{
	public static void main (String[] args) {
		ListNode one1 = new ListNode(1);
		ListNode two = new ListNode(2);
		ListNode four1 = new ListNode(4);
		one1.next = two; two.next = four1;


		ListNode one2 = new ListNode(1);
		ListNode three = new ListNode(3);
		ListNode four2 = new ListNode(4);
		one2.next = three; three.next = four2;

		one1.print();
		one2.print();
		ListNode mergedList = mergeTwoLists(one1, one2);
		mergedList.print();
	}
	MergeLists(){
		super(1);
	}
	
	public static ListNode mergeTwoLists(ListNode l1, ListNode l2) {
        if (l1 == null && l2 == null) return null;
        if (l1 == null) return l2;
        if (l2 == null) return l1;

        ListNode mergedList;
        if (l1.val > l2.val) {
            mergedList = new ListNode(l2.val);
            merge(l1, l2.next, mergedList);
        } else {
            mergedList = new ListNode(l1.val);
            merge(l1.next, l2, mergedList);
        }

        return mergedList;
    }
	public static void merge(ListNode l1, ListNode l2, ListNode parent) {
        if (l1 == null && l2 == null) return;
        if (l1 == null) {
        	parent.next = l2; 
        	return;
        }
        if (l2 == null) {
        	parent.next = l1; 
        	return;
        }
        if (l1.val > l2.val) {
        	ListNode mergee = new ListNode(l2.val);
        	parent.next = mergee;
        	merge(l1, l2.next, mergee);
        } else {
        	ListNode mergee = new ListNode(l1.val);
        	parent.next = mergee;
        	merge(l1.next, l2, mergee);
        }
    }
}
