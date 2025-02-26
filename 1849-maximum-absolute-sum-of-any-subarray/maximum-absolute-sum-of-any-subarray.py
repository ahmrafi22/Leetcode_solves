class Solution:
    def maxAbsoluteSum(self, nums: List[int]) -> int:
        # For maximum positive sum
        max_sum = 0
        curr_max = 0
        
        # For minimum negative sum
        min_sum = 0
        curr_min = 0
        
        for num in nums:
            # Kadane's algorithm for maximum sum
            curr_max = max(0, curr_max + num)
            max_sum = max(max_sum, curr_max)
            
            # Kadane's algorithm for minimum sum
            curr_min = min(0, curr_min + num)
            min_sum = min(min_sum, curr_min)
        
        return max(max_sum, abs(min_sum))