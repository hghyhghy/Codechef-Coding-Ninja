
import java.util.HashMap;

public class Missingnumber {
	
	public static int missing(int[]nums, int n) {
		
		HashMap<Integer,Boolean> map =  new HashMap<>();
		
		
		for (int num:nums) {
			
			map.put(num, true);
		}
		
		for (int i=1; i<=n ;i++) {
			
			if (!map.containsKey(i)) {
				
				return i;
			}
		}
		
		return -1;
	}
	
	public static void main(String[] args) {
		
        int[] nums = {1, 2, 4, 6, 5};
        int n = 6; // The range of numbers is 1 to n

        int missing = missing(nums, n);

        System.out.println("Array: " + java.util.Arrays.toString(nums));
        System.out.println("Missing number: " + missing);
	}
}
