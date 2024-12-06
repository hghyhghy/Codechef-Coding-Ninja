import java.util.ArrayList;
import java.util.Arrays;
import java.util.List;

public class  Consecutiveduplicate {

    public static int[] removeConsecutiveDuplicates(int[] nums) {
        if (nums == null || nums.length == 0) {
            return new int[]{};
        }

        List<Integer> result = new ArrayList<>();
        result.add(nums[0]); // Add the first element

        for (int i = 1; i < nums.length; i++) {
            if (nums[i] != nums[i - 1]) { // Compare with the previous element
                result.add(nums[i]);
            }
        }

        // Convert the list back to an array
        int[] resultArray = new int[result.size()];
        for (int i = 0; i < result.size(); i++) {
            resultArray[i] = result.get(i);
        }

        return resultArray;
    }

    public static void main(String[] args) {
        int[] nums = {1, 1, 2, 2, 3, 3, 3, 4, 4, 5};
        int[] result = removeConsecutiveDuplicates(nums);

        System.out.println("Original Array: " + Arrays.toString(nums));
        System.out.println("Array after removing consecutive duplicates: " + Arrays.toString(result));
    }
}
