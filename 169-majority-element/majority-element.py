class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        dict = {}
        for i, val in enumerate(nums):
            dict[val] = dict.get(val, 0) + 1

        for val in dict:
            if dict[val] > (len(nums)/2):
                return val 

