from itertools import accumulate
class Solution:
    def maxSumOfThreeSubarrays(self, nums: List[int], k: int) -> List[int]:
        """
        Find three non-overlapping subarrays of length k with maximum sum.
        
        Args:
            nums: List of integers
            k: Length of each subarray
        
        Returns:
            List of starting indices for the three subarrays that give maximum sum
            
        Raises:
            ValueError: If the input array is too short or k is invalid
        """
        # Input validation
        if len(nums) < 3 * k:
            raise ValueError(f"Array must be at least {3 * k} elements long")
        if k <= 0:
            raise ValueError("Subarray length must be positive")
            
        # Initialize variables to track maximum sums and their indices
        max_single_sum = 0  # Maximum sum for first window
        max_double_sum = 0  # Maximum sum for first two windows
        max_triple_sum = 0  # Maximum sum for all three windows
        
        # Initialize result indices
        idx_single = 0  # Best index for first window
        idx_double = (0, k)  # Best indices for first two windows
        idx_triple = None  # Best indices for all three windows
        
        # Calculate prefix sums for efficient window sum calculation
        prefix_sums = list(accumulate(nums, initial=0))
        
        # Iterate through all possible positions of the three windows
        for i, (start, end1, end2, end3) in enumerate(zip(
            prefix_sums,
            prefix_sums[k:],
            prefix_sums[2*k:],
            prefix_sums[3*k:]
        )):
            # Calculate current window sums
            first_window_sum = end1 - start
            second_window_sum = end2 - end1
            third_window_sum = end3 - end2
            
            # Update best single window
            if first_window_sum > max_single_sum:
                max_single_sum = first_window_sum
                idx_single = i
            
            # Update best double window
            current_double_sum = max_single_sum + second_window_sum
            if current_double_sum > max_double_sum:
                max_double_sum = current_double_sum
                idx_double = (idx_single, i + k)
            
            # Update best triple window
            current_triple_sum = max_double_sum + third_window_sum
            if current_triple_sum > max_triple_sum:
                max_triple_sum = current_triple_sum
                idx_triple = (*idx_double, i + 2*k)
        
        return list(idx_triple)  # Convert tuple to list for final result