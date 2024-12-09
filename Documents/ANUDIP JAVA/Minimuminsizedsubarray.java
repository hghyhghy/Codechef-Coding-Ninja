
public class Minimuminsizedsubarray {
	
	public static void find(int[] nums, int k) {
		
		if (k == 0|| nums.length == 0) {
			
			return;
		}
		
		for (int i=0 ;i <nums.length - k ;i ++) {
			
			int min = Integer.MAX_VALUE;
			
			for (int  j = i ;j<i+k; j++ ) {
				
				min = Math.min(min, nums[j]);
			
			}
			
			System.out.println("Subarray [" + i + " to " + (i + k - 1) + "]: Minimum = " + min);
		}
	}
	
	public static void main(String[]args) {
		
        int[] arr = {2, 5, 1, 8, 2, 9, 1};
        int k = 3;

        find(arr, k);
	}

}

