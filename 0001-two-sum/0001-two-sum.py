class Solution(object):
    def twoSum(self, nums, target):
        # Pair each number with its original index
        indexed_nums = [(nums[i], i) for i in range(len(nums))]
        # Sort by the number values
        indexed_nums.sort(key=lambda x: x[0])
        
        left = 0
        right = len(indexed_nums) - 1
        
        while left < right:
            current_sum = indexed_nums[left][0] + indexed_nums[right][0]
            if current_sum == target:
                return [indexed_nums[left][1], indexed_nums[right][1]]
            elif current_sum < target:
                left += 1
            else:
                right -= 1
        return []
