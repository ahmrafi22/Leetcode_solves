class Solution:
    def numOfSubarrays(self, arr):
        MOD = 10**9 + 7
        n = len(arr)
        dp_odd, dp_even = 0, 1
        result = 0

        for a in arr:
            if a % 2 == 0:
                dp_odd, dp_even = dp_odd, dp_even + 1
            else:
                dp_odd, dp_even = dp_even, dp_odd + 1
            result = (result + dp_odd) % MOD

        return result