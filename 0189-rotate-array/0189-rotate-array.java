class Solution {
    public void rotate(int[] nums, int k) {
        k %= nums.length;
        
        // Update the array by capturing the returned int[]
        nums = reverse(nums, 0, nums.length - 1);
        nums = reverse(nums, 0, k - 1);
        nums = reverse(nums, k, nums.length - 1);
    }

    public static int[] reverse(int[] nums, int left, int right) {
        while (left < right) {
            int temp = nums[left]; // Fixed 'ìnt' typo
            nums[left] = nums[right];
            nums[right] = temp;
            left++;
            right--;
        }
        return nums; // Added missing return statement
    }
}
