from sortedcontainers import SortedList

class Solution:
    def continuousSubarrays(self, nums: List[int]) -> int:
        # Use SortedList to efficiently track min and max in current window
        window = SortedList()
        
        total_subarrays = 0
        left = 0
        
        for right in range(len(nums)):
            # Add current element to the window
            window.add(nums[right])
            
            # Shrink window from left if max-min difference exceeds 2
            while window[-1] - window[0] > 2:
                window.remove(nums[left])
                left += 1
            
            # Count subarrays ending at current right index
            total_subarrays += right - left + 1
        
        return total_subarrays
        