class Solution:
    def countSubarrays(self, nums: List[int]) -> int:
        return sum(1 for i in range(len(nums) - 2) 
              if nums[i] + nums[i + 2] == nums[i + 1] / 2)