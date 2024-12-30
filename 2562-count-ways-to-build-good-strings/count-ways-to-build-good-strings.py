class Solution:
    def countGoodStrings(self, low: int, high: int, zero: int, one: int) -> int:
        mod = 10**9 + 7
        dp = [1] + [0] * high
        for length in range(min(zero, one), high + 1):
            dp[length] = (dp[length - zero] + dp[length - one]) % mod
        return sum(dp[low:]) % mod