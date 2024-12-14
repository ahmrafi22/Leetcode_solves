class Solution:
    def continuousSubarrays(self, nums: List[int]) -> int:
        from collections import defaultdict
        
        total_subarrays = 0
        left = 0
        count = defaultdict(int)
        
        for right in range(len(nums)):
            # Add current element to the window
            count[nums[right]] += 1
            
            # Shrink window from left while max-min > 2
            while max(count.keys()) - min(count.keys()) > 2:
                count[nums[left]] -= 1
                if count[nums[left]] == 0:
                    del count[nums[left]]
                left += 1
            
            # Count subarrays ending at current right index
            total_subarrays += right - left + 1
        
        return total_subarrays