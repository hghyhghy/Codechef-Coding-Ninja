
public class Productcountlessthank {

	public static int product(int[] array , int k) {
		
		int  n= array.length;
		int count  =0 ;
		
		for (int i =0 ; i< n ;i++) {
			
			int product = 1;
			
			for (int j = i ; j< n ; j++) {
				
				product *=  array[j];
				
				if (product < k) {
					
					count ++;
				}
				else {
					
					break;
				}
			}
		}
		
		return count;
	}
	
	public static void main(String[] args) {
		
        int[] arr = {1, 2, 3, 4, 5};
        int k = 7;
        
        int result = product(arr, k);
        
        System.out.println("Number of subarrays with product less than " + k + ": " + result);

	}
}
