
public class Maximumxor {

	public static int xor(int[] array) {
		
		int n = array.length;
		int result = 0;
		
		for (int i=0 ; i<n ;i ++) {
			
			for (int j=i+1; j<n ; j++) {
				
				int store = array[i]^array[j];
				
				result = Math.max(result,store);
			}
		}
		
		return result;
	}
	
	public static void main(String[] args) {
		
        int[] arr = {2, 5, 6};

        int result = xor(arr);
        System.out.println("Maximum XOR of any two elements in the array: " + result);
	}
}
