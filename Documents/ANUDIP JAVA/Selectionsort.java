
import java.util.Arrays;

public class Selectionsort {

	public static void selection(int[] array) {
		
		int n = array.length;
		
		for(int i = 0; i < n-1 ; i ++) {
			
			int minimum = i;
			
			for (int j =i+1; j < n; j++) {
				
				if (array[j] < array[minimum]) {
					
					minimum = j;
				}
			}
			
			int temp = array[minimum];
			array[minimum] = array[i];
			array[i]= temp;
			
			
		}
	}
	
	public static void main(String[] args) {
		
        int[] arr = {64, 25, 12, 22, 11};
        System.out.println("Original Array: " + Arrays.toString(arr));

        selection(arr);

        System.out.println("Sorted Array: " + Arrays.toString(arr));
        // Expected Output: [11, 12, 22, 25, 64]
	}
}
