public class linearsearch {

    public  static  int linearsearch(int[] arr, int target){

        for  (int  i=0; i < arr.length ; i++){

            if (arr[i] ==  target){

                return  i;
            }
        }

        return -1;


    }

    public static  void  main(String[] args){

        int[] numbers = {10, 20, 30, 40, 50};
        int target = 30;

        // Perform linear search
        int result = linearsearch(numbers, target);

        // Print the result
        if (result != -1) {
            System.out.println("Element found at index: " + result);
        } else {
            System.out.println("Element not found in the array.");
        }
    }
}
