
import java.util.ArrayList;
import java.util.List;

public class Commonelement {
	
	public static List<Integer> common(int[]arr1,int[]arr2){
		
		List<Integer> store = new ArrayList<>();
		
		for (int i=0; i<arr1.length;i++) {
			
			for (int j=0;j<arr2.length;j++) {
				
				if (arr1[i] == arr2[j]) {
					
					if (!store.contains(arr1[i])) {
						
						store.add(arr1[i]);
					}
				}
			}
		}
		
		return store;
	}
	
	public static void main(String[]args) {
		
        int[] arr1 = {1, 2, 3, 4, 5};
        int[] arr2 = {3, 4, 5, 6, 7};

        List<Integer> result = common(arr1, arr2);

        System.out.println("Common elements: " + result);
	}

}
