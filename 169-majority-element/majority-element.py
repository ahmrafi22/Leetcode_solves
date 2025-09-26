class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        seen = {}
        for i in nums:
            if i in seen:
                seen[i] += 1
            else:
                seen[i] = 1
        return max(seen, key=seen.get)