
class TreeNode{
	
	int val;
	TreeNode left,right;
	
	TreeNode(int val){
		
		this.val=val;
		this.left=null;
		this.right=null;
	}
}

public class Heightofthtree {

	public static int heightoftree(TreeNode root) {
		
		if (root == null) {
			
			return 0;		
			
		}
		
		int leftheight = heightoftree(root.left);
		int rightheight = heightoftree(root.right);
		
		return 1+Math.max(leftheight, rightheight);
		
	}
	
	public static void main(String[] args) {
		
        TreeNode root = new TreeNode(1);
        root.left = new TreeNode(2);
        root.right = new TreeNode(3);
        root.left.left = new TreeNode(4);
        root.left.right = new TreeNode(5);

        System.out.println("Height of the tree: " + heightoftree(root));
	}
}
