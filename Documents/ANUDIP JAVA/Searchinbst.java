
class Node{
	
	int value;
	Node left,right;
	
	public Node(int value) {
		
		this.value = value;
		left=right=null;
	}
}

public class Searchinbst {

	public static boolean search(Node root, int target) {
		
			if (root == null) {
				
				return false;
			}
			
			if (root.value  ==  target) {
				
				return  true;
			}
			
			if (target < root.value) {
				
				return search(root.left, target);
			} else {
				
				return search(root.right, target);
			}
			
	}
	
	public static void main(String[] args) {
		
        Node root = new Node(15);
        root.left = new Node(10);
        root.right = new Node(20);
        root.left.left = new Node(8);
        root.left.right = new Node(12);
        root.right.left = new Node(17);
        root.right.right = new Node(25);

        int target = 12;

        if (search(root, target)) {
            System.out.println("Element " + target + " found in the BST.");
        } else {
            System.out.println("Element " + target + " not found in the BST.");
        }
	}
}
