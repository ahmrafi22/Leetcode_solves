class Solution:
    def maxAbsoluteSum(self, nums: List[int]) -> int:
        maxSum = 0
        minSum = 0
        for i in nums:
            maxSum = max(0, maxSum + i)
            minSum = min(0, minSum + i)
        return maxSum - minSum