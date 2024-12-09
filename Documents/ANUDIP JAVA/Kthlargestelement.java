import java.util.*;

public class Kthlargestelement {

    public static int largestSum(int[] array, int k) {
        List<Integer> store = new ArrayList<>();
        int n = array.length;

       
        for (int i = 0; i < n; i++) {
            int current = 0;

            for (int j = i; j < n; j++) {
                current += array[j];
                store.add(current);
            }
        }

        Collections.sort(store, Collections.reverseOrder());


        if (k <= store.size()) {
            return store.get(k - 1);
        } else {
            return -1; 
            }
    }

    public static void main(String[] args) {
        int[] arr = {1, -2, 3, -4, 5};
        int K = 2;

        int result = largestSum(arr, K);
        System.out.println("The " + K + "th largest sum subarray is: " + result);
        
    }
}
