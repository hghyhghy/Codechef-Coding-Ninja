
import java.util.ArrayList;

public class Intersection {
	
	public static int[] common(int[] arr1 , int[]arr2) {
		
		ArrayList<Integer> store = new ArrayList<>();
		
		for (int i = 0; i <arr1.length ; i++) {
			
			for (int j = 0; j <arr2.length ; j++) {
				
				if (arr1[i] == arr2[j] && !store.contains(arr1[i])) {
					
					store.add(arr1[i]);
					break;
				}
			}
		}
		
        int[] result = new int[store.size()];
        for (int i = 0; i < store.size();i++ ) {
            result[i] = store.get(i);
        }
        return result;
		
	}
	
	  public static void main(String[] args) {
	        int[] arr1 = {1, 2, 2, 3, 4};
	        int[] arr2 = {2, 3, 3, 5};

	        int[] intersection = common(arr1, arr2);

	        System.out.println("Array 1: " + java.util.Arrays.toString(arr1));
	        System.out.println("Array 2: " + java.util.Arrays.toString(arr2));
	        System.out.println("Intersection: " + java.util.Arrays.toString(intersection));
	    }

}
