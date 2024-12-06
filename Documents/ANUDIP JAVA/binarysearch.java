
import  java.util.Arrays;

public class binarysearch {

    public  static  void  main(String[] args){

        int[] arr = {2, 3, 4, 10, 40, 50, 60};
        int target = 10;

        // Perform Binary Search
        int result = binarySearch(arr, target);

        // Print the result
        if (result == -1) {
            System.out.println("Element not found in the array.");
        } else {
            System.out.println("Element found at index: " + result);
        }
    }

    public  static int binarySearch(int[] arr, int target){

        int left = 0;
        int right = arr.length - 1;

        while ( left <= right){

            int mid = (left+right) / 2;

            if  ( arr[mid] == target){

                return  mid;
            }

            if (arr[mid] > target){

                right = mid -1;
            }
            else {

                left =mid +1;
                }
        }

        return -1;
    }
}
