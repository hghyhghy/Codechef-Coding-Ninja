
public class Sumofevenindex {

	
	public static int  total(int[] array) {
		
		int sum =0 ;
		
		for (int i=0 ; i<array.length ;i ++) {
			
			if (i%2 == 0) {
				
				sum += array[i];	
			}
		}
		
		return sum;
	}
	
	public static void main(String[] args) {
		
        int[] arr = {2, 5, 8, 11, 4, 7, 6};

        int result = total(arr);
        System.out.println("Sum of elements at even indices: " + result);
	}
}
