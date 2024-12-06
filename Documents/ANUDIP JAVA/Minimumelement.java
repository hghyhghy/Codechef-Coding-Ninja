

public class Minimumelement {

	public static int find(int[] nums) {
		
		int min = Integer.MAX_VALUE;
		
		for (int i=0; i<nums.length ; i++) {
			
			if (nums[i] < min) {
				
				min = nums[i];
			}
		}
		
		return min;
	}
	
	public static void main(String[] args) {
		
        int[] arr = {3, 5, 1, 8, 2, 9, 0};

        int result = find(arr);

        System.out.println("The minimum number in the array is: " + result);
	}
}
