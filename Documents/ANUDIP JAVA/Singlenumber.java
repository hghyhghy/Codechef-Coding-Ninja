
import java.util.HashMap;

public class Singlenumber {
	
	public static int occurance(int[] nums) {
		
		HashMap<Integer, Integer> map = new HashMap<>();
		
		
		for (int num:nums) {
			
			map.put(num, map.getOrDefault(num,0) +1);
			
			
		}
		
		for (int key : map.keySet()) {
			
			if(map.get(key) == 1) {
				
				return key;
			}
		}
		
		return -1;
	}
	
	public static void main(String[] args) {
		
        int[] nums = {4, 3, 2, 4, 1, 3, 2};

        int singleNumber = occurance(nums);

        System.out.println("Array: " + java.util.Arrays.toString(nums));
        System.out.println("Number with single occurrence: " + singleNumber);
	}

}
