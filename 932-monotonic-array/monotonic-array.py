class Solution:
    def isMonotonic(self, nums: List[int]) -> bool:
        flag_inc= False
        flag_dec = False
        for i in range(1,len(nums)):
            if nums[i]> nums[i-1]:
                flag_inc= True
            if nums[i]<nums[i-1]:
                flag_dec = True
        if flag_inc and flag_dec:
            return False
        return True
        