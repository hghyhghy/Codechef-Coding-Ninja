

public class Maximumsubarraywithzerosum {
	
	public static int zerosum(int[] nums) {
		
		int maxlength = 0;
		
		for (int i=0 ;i<nums.length ; i++) {
			
			int sum = 0;
			
			for (int j= i; j <nums.length ;j ++) {
				
				sum += nums[j];
				
				if (sum == 0) {
					
					maxlength = Math.max(maxlength, j-i+1);
				}
			}
		}
		
		return maxlength;
	}
	
	public static void main(String[]args) {
		
		 int[] arr = {1, 2, -3, 3, 1, -4, 2, 1, -1, -2};

	        int maxLength = zerosum(arr);

	        System.out.println("The length of the longest subarray with zero sum is: " + maxLength);
	}
}
