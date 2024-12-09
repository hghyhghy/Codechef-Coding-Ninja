
class ListNode{
	
	int val;
	ListNode next;
	
	ListNode(int val){
		
		this.val=  val;
		this.next  = null;
	}
}

public class Reverselist {
	
	public static void reverselist(ListNode root) {
		
		if (root == null) {
			
			return ;
		}
		
		reverselist(root.next);
		
		System.out.println(root.val + " ");
		
	}
	
	public static  void main(String[] args) {
		
        // Create a sample linked list: 1 -> 2 -> 3 -> 4
        ListNode head = new ListNode(1);
        head.next = new ListNode(2);
        head.next.next = new ListNode(3);
        head.next.next.next = new ListNode(4);

        // Print the list in reverse order
        System.out.println("Reversed List:");
        reverselist(head); // Expected Output: 4 3 2 1
	}

}
