public class Twosum1 {

    public static int[] twosum(int[] array, int target) { // Change return type to int[]
        int left = 0;
        int right = array.length - 1;

        while (left < right) {
            int current = array[left] + array[right];

            if (current == target) {
                return new int[]{left, right}; // Return an array of indices
            } else if (current < target) {
                left++;
            } else {
                right--;
            }
        }

        return new int[]{-1, -1}; // Return {-1, -1} if no valid pair is found
    }

    public static void main(String[] args) {
        int[] arr = {1, 2, 3, 4, 5};
        int target = 8;

        int[] result = twosum(arr, target);

        if (result[0] != -1) {
            System.out.println("Indices: " + result[0] + " " + result[1]);
        } else {
            System.out.println("No pair found with the given target.");
        }
    }
}
