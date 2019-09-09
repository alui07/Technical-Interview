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
}