
public class Palindrome {
	
	public static boolean ispalindrome(String str) {
		
		str =str.toLowerCase();
		
		String  reversed = "";
		for (int i=str.length()-1 ; i>=0 ; i--) {
			
			reversed += str.charAt(i);
		}
		
		return str.equals(reversed);
 	}
	
	
	public static void main(String[] args) {
		
		String input = "Madam";
		
        if (ispalindrome(input)) {
            System.out.println("\"" + input + "\" is a palindrome.");
        } else {
            System.out.println("\"" + input + "\" is not a palindrome.");
        }
	}
}
