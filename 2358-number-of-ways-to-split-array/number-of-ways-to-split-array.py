class Solution:
    def waysToSplitArray(self, nums: List[int]) -> int:
        self.nums=nums
        total=sum(nums)
        left_sum=0
        count=0
        for i in range(0,len(nums)-1):
            left_sum+=nums[i]
            right_sum=total-left_sum
            if left_sum>=right_sum:
                count+=1
        return count