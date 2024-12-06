
import java.util.Iterator;
import java.util.Scanner;

public class Evenodd {

	public static void main(String[] args) {
		
		Scanner scanner =  new Scanner(System.in);
		System.out.print("Enter the number of elements: ");
		
		int n = scanner.nextInt();
		
		int[] arr = new int[n];
		System.out.println("Enter the elements:");
		
		 for(int i =0 ;i < n ; i++) {
			 
			 arr[i] = scanner.nextInt();
		 }
		 
		 System.out.println("Even and Odd elements in the array:");
		 
		 for (int i=0 ; i <n ; i++) {
			 
			 if (arr[i] % 2 == 0) {
				 
				 System.out.println(arr[i] + " is even.");
				 
			 }
			 
			 else {
				 
				 System.out.println(arr[i] + " is odd.");
			 }
		 }
	}

}
