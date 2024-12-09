
public class Counttriplets {
	
	public static int count(int[] array ,  int target) {
		
		int n =  array.length;
		int count   =0 ;
		
		for (int  i = 0 ; i < n ; i++) {
			
			for (int j =i+1 ; j<n ;j ++) {
				
				for (int k=j+1 ; k <n ;k++) {
					
					if (array[i]+array[j]+array[k] < target) {
						
						count ++;
					}
				}
			}
		}
		
		return count;
	}
	
	public static void main(String[] args) {
		
        int[] arr = {1, 5, 2, 3, 4, 6, 7};
        int target = 9;
        int result = count(arr, target);
        
        System.out.println("Number of triplets with sum less than " + target + ": " + result);
	}

}
