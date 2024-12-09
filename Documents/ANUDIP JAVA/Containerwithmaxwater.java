public class Containerwithmaxwater {

    public static int maxArea(int[] array) {
        int n = array.length;
        int left = 0, right = n - 1;
        int maxArea = Integer.MIN_VALUE;

        while (left < right) {
            // Calculate the height and width of the container
            int height = Math.min(array[left], array[right]);
            int width = right - left;

            // Calculate the area
            int area = height * width;

            // Update maxArea if the current area is greater
            maxArea = Math.max(maxArea, area);

            // Move the pointers to try for a larger area
            if (array[left] < array[right]) {
                left++;
            } else {
                right--;
            }
        }

        return maxArea;
    }

    public static void main(String[] args) {
        int[] arr = {1, 8, 6, 2, 5, 4, 8, 3, 7};
        int result = maxArea(arr);
        System.out.println("Maximum area: " + result); // Output: 49
    }
}
