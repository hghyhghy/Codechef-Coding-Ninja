
public class targetelement {


    public static  void main(String[] args){

        int[] number = {2, 4, 6, 8, 10, 12};
        int target = 10;

        int index = find(number,target);
        if (index != -1) {
            System.out.println("Target " + target + " found at index: " + index);
        } else {
            System.out.println("Target " + target + " not found in the array.");
        }
    }

    public  static  int find(int[] arr,int target){

        for (int i= 0; i < arr.length ; i ++){

            if (arr[i] ==  target){

                return  i;
            }
        }

        return  -1;
    }
}
