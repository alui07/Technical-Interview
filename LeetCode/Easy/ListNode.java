public class ListNode{
	int val;
	ListNode next;
	ListNode(int x) {
		val = x;
	}
	public String printNode() {
		if (this.next == null) return Integer.toString(this.val);
		return Integer.toString(this.val) + "->" + this.next.printNode();
	}

	public void print() {
		System.out.println(this.printNode());
	}

	public static void main (String[] args) {
		ListNode one = new ListNode(1);
		ListNode two = new ListNode(2);
		ListNode three = new ListNode(3);
		one.next = two;
		two.next = three;
		System.out.println(one.printNode());
	}
	public static ListNode mergeTwoLists(ListNode l1, ListNode l2) {
        if (l1 == null && l2 == null) return null;
        if (l1 == null) return l2;
        if (l2 == null) return l1;
        ListNode mergedList = new ListNode(-1);
        mergedList.merge(l1, l2);
        return mergedList;
    }
	public void merge(ListNode l1, ListNode l2) {
        if (l1 == null && l2 == null) return;
        if (l1 == null) {
        	this.next = l2; 
        	return;
        }
        if (l2 == null) {
        	this.next = l1; 
        	return;
        }
        if (l1.val > l2.val) {
        	ListNode mergee = new ListNode(l2.val);
        	this.next = mergee;
        	mergee.merge(l1, l2.next);
        } else {
        	ListNode mergee = new ListNode(l1.val);
        	this.next = mergee;
        	mergee.merge(l1.next, l2);
        }
    }
}