
public class Evensum {
	
	public static int total(int[] nums) {
		
		int sum = 0;
		
		for (int num:nums) {
			
			if (num % 2 == 0) {
				
				sum += num;
			}
		}
		
		return sum;
	}
	
	public static void main(String[] args) {
		
        int[] nums = {1, 2, 3, 4, 5, 6, 7, 8, 9, 10};
        int result = total(nums);

        System.out.println("Array: " + java.util.Arrays.toString(nums));
        System.out.println("Sum of even numbers: " + result);
    
	}

}