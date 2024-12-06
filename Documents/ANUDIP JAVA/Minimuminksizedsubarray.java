public class Minimuminksizedsubarray {

    public static int subarray(int[] nums, int k) {
        // If the array size is less than k, return -1 or a meaningful message
        if (nums.length < k) {
            System.out.println("Array size must be greater than or equal to k");
            return -1;
        }

        int min = Integer.MAX_VALUE;

        for (int i = 0; i <= nums.length - k; i++) {
            int sum = 0;

            for (int j = i; j < i + k; j++) {
                sum += nums[j];
            }

            min = Math.min(min, sum);
        }

        return min;
    }

    public static void main(String[] args) {
        int[] arr = {2, 5, 1, 8, 2, 9, 1};
        int k = 3;

        int result = subarray(arr, k);

        if (result != -1) {
            System.out.println("Minimum sum of a subarray of size " + k + " is: " + result);
        }
    }
}
