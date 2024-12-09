import java.util.*;

public class Distinctpalindrome {
	
	public static boolean ischeck(String str) {
		
		int i=0;
		int j=str.length();
		
		while (  i<j) {
			
			if (str.charAt(i) !=  str.charAt(j)) {
				
				return false;
			}
			
			i ++;
			j --;
		}
		
		return true;
	}
	
	public static List<String> finding(String s){
		
		int n = s.length();
	}

}
