class Solution:
    def check(self, nums: List[int]) -> bool:

        rotations = sum(nums[i] < nums[i-1] for i in range(len(nums)))

        return rotations <= 1