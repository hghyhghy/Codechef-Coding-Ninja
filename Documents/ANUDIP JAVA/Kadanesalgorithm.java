
public class Kadanesalgorithm {
	
	public static int algorithm(int[] nums) {
		
		int total = 0;
		int max =Integer.MIN_VALUE;
		
		for (int  num : nums) {
			
			total += num;
			
			if (total > max) {
				
				max = total;
			}
			
			if (total < 0 ) {
				
				total = 0;
			}
		}
		
		return max;
	}
	
	public static void main(String[] args) {
		
        int[] arr = {1, 2, -3, 4, 5};

        int result = algorithm(arr);
        System.out.println("Maximum possible sum of a subarray is: " + result);
	}

}
