
import java.util.Arrays;

public class Minimumdifference {
	
	public static int difference(int[] array) {
		
		int n =array.length;
		
		Arrays.sort(array);
		int minimum = Integer.MAX_VALUE;
		
		for(int i=0;i<n-1;i++) {
			
			int diff = Math.abs(array[i]-array[i+1]);
			
			minimum=Math.max(minimum, diff);
			
			
		}
		
		return minimum;
	}
	
	public static void main(String[] args) {
		
        int[] arr = {3, -6, 7, -7, 0};
        int result = difference(arr);
        System.out.println("Minimum absolute difference: " + result);
	}

}
