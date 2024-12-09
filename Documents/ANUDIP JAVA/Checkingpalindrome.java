
public class Checkingpalindrome {

	public  static  boolean check(String str) {
		
		int start = 0;
		int end  =  str.length()-1;
		
		while (start < end) {
			
			if (str.charAt(start) !=  str.charAt(end)) {
				
				return false;
			}
			
			start ++;
			end -- ;
			
			
		}
		
		return true;
	}
	
	public  static void main(String[] args) {
		
        String s1 = "madam";
        String s2 = "hello";

        System.out.println("Is '" + s1 + "' a palindrome? " + (check(s1) ? "YES" : "NO"));
        System.out.println("Is '" + s2 + "' a palindrome? " + (check(s2) ? "YES" : "NO"));
	}
}
