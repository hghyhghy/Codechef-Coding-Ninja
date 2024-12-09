
public class Buysellstock {
	
	public static int profit(int[]array) {
		
		int  n = array.length;
		int max = 0;
		
		for(int i=0;i<n-1 ;i++) {
			
			if (array[i+1] > array[i]) {
				
				max += array[i+1] - array[i];
			}
		}
		
		return max;
	}
	
	public static void main(String[] args) {
		
        int[] prices = {7, 1, 5, 4, 3, 6};
        int result = profit(prices);
        System.out.println("Maximum profit: " + result);
	}

}
