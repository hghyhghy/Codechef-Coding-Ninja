
public class Ciuntpairwithsum {
	
	public static int count(int[]nums, int target) {
		
		int count = 0 ;
		
		for (int i=0;i<nums.length;i++) {
			
			for (int j=i+1;j<nums.length;j++) {
				
				if (nums[i]+nums[j] ==  target) {
					
					count ++;
				}
			}
		}
		
		return count;
	}
	
	public static void main(String[] args) {
		
        int[] nums = {1, 5, 7, -1, 5};
        int target = 6;

        int result = count(nums, target);

        System.out.println("Array: " + java.util.Arrays.toString(nums));
        System.out.println("Count of pairs with sum " + target + ": " + result);
	}

}
