import java.util.*;
import java.lang.*;

public class MergeLists extends ListNode{
	public static void main (String[] args) {

	}
	MergeLists(){
		super(1);
	}
	public ListNode mergeTwoLists(ListNode l1, ListNode l2) {
        if (l1 == null && l2 == null) return null;
        if (l1 == null) return l2;
        if (l2 == null) return l1;
        ListNode mergedList = new ListNode(-1);
        //the case where both l1 and l2 exist

        while (curr_l1.next != null || curr_l2.next != null) {

        }
        return mergedList;
    }
}
