from collections import defaultdict

class Solution:
    def maximumSum(self, nums: List[int]) -> int:
        max_seen = defaultdict(lambda: 0)
        ans = -float('inf')
        for i in nums:
            digit_sum = sum(int(digit) for digit in str(i))
            if digit_sum in max_seen:
                ans = max(max_seen[digit_sum] + i, ans)
            if i > max_seen[digit_sum]:
                max_seen[digit_sum] = i
        return ans if ans != -float('inf') else -1