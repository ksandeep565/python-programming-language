class Solution {
    public void moveZeroes(int[] nums) {
        int n = nums.length;
        // Move non-zero elements to the front
        int j = 0;

        for (int i = 0; i < n; i++) {
            if (nums[i] != 0) {
                nums[j] = nums[i];
                j++;
            }
        }

        // Fill remaining positions with 0
        while (j < n) {
            nums[j] = 0;
            j++;
        }

        // Print array
        for (int i : nums) {
            System.out.print(i + " ");
        }

    
    }
}