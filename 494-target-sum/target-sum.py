class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        total = sum(nums)
        
        # Early termination checks
        if total < abs(target):
            return 0
        
        # Check if target sum is achievable
        required_sum = total + target
        if required_sum % 2:  # If odd, no solution possible
            return 0
            
        target_sum = required_sum // 2
        
        # Optimize space: only need previous row
        dp = [0] * (target_sum + 1)
        dp[0] = 1
        
        # Fill dp array
        for num in nums:
            for j in range(target_sum, num - 1, -1):
                dp[j] += dp[j - num]
        
        return dp[target_sum]