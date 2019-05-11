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
}
