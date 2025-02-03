class Solution:
   def longestMonotonicSubarray(self, nums: List[int]) -> int:
       max_len = 1
       curr_up = curr_down = 1
       
       for i in range(1, len(nums)):
           if nums[i] > nums[i-1]:
               curr_up += 1
               curr_down = 1
           elif nums[i] < nums[i-1]:
               curr_down += 1
               curr_up = 1
           else:
               curr_up = curr_down = 1
           
           max_len = max(max_len, curr_up, curr_down)
       
       return max_len