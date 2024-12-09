import java.util.*;

public class Substringwithkchar {
	
	public static int substring(String string , int k) {
		
		int n = string.length();
		int maximum = 0;
		
		for (int i = 0; i < n; i++) {
			
			Set<Character> seen = new HashSet<>();
			
			for (int j = i; j < n ; j ++) {
				
				seen.add(string.charAt(j));
				
				if (seen.size() > k) {
					
					break;
				}
				
				maximum = Math.max(maximum, j-i+1);
			}
		}
		
		return maximum;
	}
	
	public static void main(String[] args) {
		
        String S = "bacda";
        int K = 3;

        int result = substring(S, K);
        System.out.println("The maximum size of a good substring is: " + result);
        // Expected output: 4
	}

}
