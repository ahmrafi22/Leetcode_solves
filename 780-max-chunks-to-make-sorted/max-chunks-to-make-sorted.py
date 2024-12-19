from typing import List

class Solution:
    def maxChunksToSorted(self, arr: List[int]) -> int:
        """
        Determines the maximum number of chunks an array can be split into such that
        when each chunk is sorted individually, the entire array becomes sorted.
        
        The key insight is that for a valid chunk from index 0 to i:
        1. The maximum value in that chunk must be i
        2. All elements 0 to i must be present in that chunk
        
        Time Complexity: O(n) where n is length of input array
        Space Complexity: O(1) as we only use a few variables
        
        Args:
            arr: List[int] - Input array containing permutation of numbers from 0 to n-1
            
        Returns:
            int: Maximum number of chunks possible
        
        Example:
            Input: [1,0,2,3,4]
            Output: 2
            Explanation: We can split into two chunks: [1,0] and [2,3,4]
        """
        if not arr:
            return 0
            
        chunk_count = curr_max = 0
        
        for i, num in enumerate(arr):
            # Keep track of maximum value seen so far
            curr_max = max(curr_max, num)
            
            # If current maximum equals current index, we've found a valid chunk
            # This ensures all required elements (0 to i) are present
            if curr_max == i:
                chunk_count += 1
                
        return chunk_count