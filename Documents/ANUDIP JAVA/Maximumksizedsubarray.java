
import java.util.ArrayList;

public class Maximumksizedsubarray {
	
	public static ArrayList<Integer> subarray(int[] nums , int k){
		
		ArrayList<Integer> storeArrayList = new ArrayList<>();
		
		for (int i= 0; i < nums.length - k; i++) {
			
			int max = nums[i];
			
			for (int  j = i ; j<i+k ;j ++) {
				
				if (nums[j] > max) {
					
					max = nums[j];
				}
			}
			
			storeArrayList.add(max);
		}
		
		return storeArrayList;
	}
	
	public static void main(String[]args) {
		
        int[] arr = {1, 3, 2, 5, 8, 7, 6, 4};
        int k = 3;

        ArrayList<Integer> result = subarray(arr, k);

        System.out.println("Array: " + java.util.Arrays.toString(arr));
        System.out.println("Maximum in each subarray of size " + k + ": " + result);
	}

}
