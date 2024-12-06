
import java.util.HashSet;
import java.util.Iterator;

public class Majorityelement {

	public static int majority(int[] nums) {
		
		HashSet<Integer> unique = new HashSet<>();
		
		for (int num:nums) {
			
			unique.add(num);
		}
		
		int limit = nums.length/2;
		
		for(int element : unique) {
			
			int count = 0;
			
			for(int num : nums) {
				
				if  (num == element) {
					
					count ++;
				}
			}
			
			if (count > limit) {
				
				return element;
			}
		}
	}
	
	public static void main(String[] args) {
		
		int[] nums = {2, 2, 1, 1, 1, 2, 2};
		
        try {
            int majorityElement = majority(nums);
            System.out.println("The majority element is: " + majorityElement);
        } catch (IllegalArgumentException e) {
            System.out.println(e.getMessage());
        }
	}
}
