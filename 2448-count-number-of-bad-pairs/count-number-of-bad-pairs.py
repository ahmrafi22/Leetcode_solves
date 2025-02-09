class Solution:
    def countBadPairs(self, nums: List[int]) -> int:
        n = len(nums)
        from collections import Counter
        count = Counter(x - i for i, x in enumerate(nums))
        good = sum(v * (v - 1) >> 1 for v in count.values())
        return (n * (n - 1) >> 1) - good