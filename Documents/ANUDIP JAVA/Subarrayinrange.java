
public class Subarrayinrange {

	public static int range(int[] array,int x, int y) {
		
		int n=array.length;
		int count =0 ;
		
		for(int i=0;i<n;i++) {
			
			int maximum=array[i];
			
			for(int j =i;j<n;j++) {
				
				maximum=Math.max(maximum, array[j]);
				
				if(maximum >=x && maximum<=y) {
					
					count ++;
				}
			}
		}
		
		return count;
	}
	
	public static void main(String[] args) {
		
        int[] arr = {1, 2, 3, 4, 5};
        int X = 2;
        int Y = 4;

        int result = range(arr, X, Y);
        System.out.println("Number of subarrays with max element between " + X + " and " + Y + ": " + result);
	}
}
