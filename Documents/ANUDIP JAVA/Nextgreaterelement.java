import java.util.*;

public class Nextgreaterelement {

	public static int[] nextgreater(int[] array) {
		
		int n =  array.length;
		int[] result= new int[n];
		
		Arrays.fill(result, -1);
		
		for (int i = 0 ; i < n ; i ++) {
			
			for (int j = i+1; j < n ; j++) {
				
				if (array[j] > array[i]) {
					
					result[i] = array[j];
					break;
				}
			}
		}
		
		return result;
	}
	
	public static void main(String[] args) {
		
        int[] arr = {1, 3, 2};
        int[] nge = nextgreater(arr);

        // Print the result array
        System.out.println("Next Greater Elements: " + Arrays.toString(nge));
	}
}

