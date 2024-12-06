
import java.util.ArrayList;
import java.util.List;


public class Threesum {
	
	public static List<int[]> find(int[]nums, int target){
		
		List<int[]> result = new ArrayList<>();
		
		for (int i=0; i<nums.length ; i++) {
			
			for (int j= i+1; j<nums.length ; j++) {
				
				for (int k = j+1 ; k < nums.length ; k ++) {
					
					if (nums[i]+nums[j]+nums[k] == target) {
						
						result.add(new int[] {i,j,k});
					}
				}
			}
		}
		
		return result;
	}
	
	public static void main(String[] args) {
		
        int[] nums = {2, 7, 11, 15, -5, 3};
        int target = 9;

        List<int[]> results = find(nums, target);

        if (results.isEmpty()) {
            System.out.println("No solution found.");
        } else {
            System.out.println("Triplets with indices:");
            for (int[] triplet : results) {
                System.out.println("[" + triplet[0] + ", " + triplet[1] + ", " + triplet[2] + "]");
            }
        }
	}

}
