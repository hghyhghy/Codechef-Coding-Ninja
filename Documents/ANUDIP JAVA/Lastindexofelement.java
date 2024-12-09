
public class Lastindexofelement {

	public static int index(int[] array , int x) {
		
		int n = array.length;
		int last = -1;
		
		for (int i=n-1; i >=0 ; i--) {
			
			if (array[i] == x) {
				
				last = i;
				break;
			}
		}
		
		return last;
	}
	
	public static void main(String[] args) {
		
        int[] arr = {1, 2, 3, 2, 5, 2, 7};
        int x = 2;

        int result = index(arr, x);
        System.out.println("The last occurrence of " + x + " is at index: " + result);
        // Output: The last occurrence of 2 is at index: 5
	}
}
