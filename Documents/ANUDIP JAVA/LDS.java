import java.util.ArrayList;
import java.util.concurrent.Flow.Publisher;


public class LDS {
	
	public static int find(int[] array) {
		
		ArrayList<Integer> store = new ArrayList<>();
		
		for (int num:array) {
			
			if(store.isEmpty() || store.get(store.size()-1) > num) {
				
				store.add(num);
			}
			else {
				
				for (int i= 0 ; i<store.size() ; i++) {
					
						if (store.get(i) <= num) {
							
							store.set(i, num);
							break;
						}
				}
			}
		}
		
		return store.size();
	
	}

	
	public static void main(String[] args) {
		
        int[] arr = {5, 0, 3, 2, 9};
        int result = find(arr);
        System.out.println("Length of the longest decreasing subsequence: " + result);
	}
}
