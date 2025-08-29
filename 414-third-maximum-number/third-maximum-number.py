class Solution:
    def thirdMax(self, nums: List[int]) -> int:
        arr = list(set(nums))
        arr.sort(reverse=True)
        if len(arr) < 3:
            return arr[0]
        return arr[2]