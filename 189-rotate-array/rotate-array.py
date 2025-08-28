class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        n = len(nums)
        k = k % n  
        
        for i in range(k):
            last_element = nums[-1]
            nums.insert(0, last_element)
            nums.pop()