import java.util.*;

public class Substringhavingkchar {

    public static int countchar(String str, int k) {
        int n = str.length();
        int count = 0;

        for (int i = 0; i < n; i++) {
            Set<Character> store = new HashSet<>();

            for (int j = i; j < n; j++) {
                store.add(str.charAt(j));

                if (store.size() == k) {
                    count++;
                } else if (store.size() > k) {
                    break;
                }
            }
        }

        return count;
    }

    public static void main(String[] args) {
        String str = "abcad";
        int k = 2;

        // Get the result
        int result = countchar(str, k);

        // Print the result
        System.out.println("The count of substrings with exactly " + k + " distinct characters is: " + result);
    }
}
