
import java.util.*;

public class Longestsubstring {
	
	public static int substring(int[] nums) {
		
		int n = nums.length;
		int maxlen = 0 ;
		
		for (int i=0 ; i <n ; i++) {
			
			
			Set<Integer> seen = new HashSet<>();
			
			for (int j =i; j<n ; j++) {
				
				seen.add(nums[j]);
				
				if (seen.size() > 2) {
					
					break;
				}
				
				maxlen = Math.max(maxlen, j-i+1 );
			}
		}
		
		return maxlen;
	}

	
	public static void main(String[] args) {
		
        int[] fruits = {1, 2, 1, 3, 2};
        int result = substring(fruits);
        System.out.println("Longest subarray with at most two distinct integers has length: " + result);
	}
}
