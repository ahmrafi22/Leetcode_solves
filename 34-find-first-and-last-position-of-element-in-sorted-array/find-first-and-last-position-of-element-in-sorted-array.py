import bisect

class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        def helper(nums, target):
            left = bisect.bisect_left(nums, target)
            right = bisect.bisect_right(nums, target) - 1
            
            if left <= right and left < len(nums) and nums[left] == target:
                return [left, right]
            return [-1, -1]
        
        return helper(nums, target)  