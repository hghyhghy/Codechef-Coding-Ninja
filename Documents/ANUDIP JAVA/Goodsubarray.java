
import java.util.*;

public class Goodsubarray {
	
	public static int count(int[] arr , int k) {
		
		int n=  arr.length;
		int count  =0 ;
		
		for (int i=0 ; i< n ;i++) {
			
			Set<Integer> store = new HashSet<>();
			
			for (int j = i ; j<n ; j++) {
				
				store.add(arr[j]);
				
				if (store.size() == k ) {
					
					count ++;
				}
				else if (store.size() > k) {
					
					break;
					
				}
			}
		}
		
		return count;
	}
	
	public static void main(String[] args) {
		
        int[] arr = {1, 3, 1, 1, 2};
        int k = 2;

        int result = count(arr, k);
        System.out.println("Number of good subarrays: " + result);
	}

}
