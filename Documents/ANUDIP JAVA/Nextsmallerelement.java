
import java.util.Arrays;

public class Nextsmallerelement {
	
	public static int[] smaller(int[] nums) {
		
		int n= nums.length;
		int[] store = new int[n];
		
		for (int i=0;i<n;i++) {
			
			int next =-1;
			
			for (int j=i+1;j<n;j++) {
				
				if (nums[j] < nums[i]) {
					
					next = nums[j];
					break;
				}
			}
			
			store[i] = next;
		}
		
		return store;
	}
	
	public static void main(String[] args) {
		
        int[] arr = {4, 8, 5, 2, 25};

        int[] result = smaller(arr);

        System.out.println("Next smaller elements array: " + Arrays.toString(result));
	}

}
