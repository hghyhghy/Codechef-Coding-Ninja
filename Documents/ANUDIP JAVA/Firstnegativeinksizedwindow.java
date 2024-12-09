
import java.util.ArrayList;
import java.util.List;

public class Firstnegativeinksizedwindow {
	
	public static List<Integer> find(int[] array ,int k){
		
		int n = array.length;
		List<Integer> storeIntegers =new ArrayList<>();
		
		for ( int i=0 ; i< n-k ; i++) {
			
			int  min = 0;
			
			for (int j=i ; j<i+k ; j++) {
				
				if (array[j] < min) {
					
					min = array[j];
					break;
				}
			}
			
			storeIntegers.add(min);
		}
		
		return storeIntegers;
	}
	
	public static void main(String[] args) {
		
        int[] arr = {5, -3, 2, 3, -4};
        int k = 2;

        List<Integer> result = find(arr, k);

        System.out.println("First negative element in every window of size " + k + " is: " + result);
	}

}
