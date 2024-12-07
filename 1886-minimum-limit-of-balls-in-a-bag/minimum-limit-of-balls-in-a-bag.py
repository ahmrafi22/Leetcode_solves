class Solution:
    def minimumSize(self, nums: List[int], maxOperations: int) -> int:
            left = 1  # Minimum possible bag size
            right = max(nums)  # Maximum initial bag size
            
            def can_reduce_to_max_size(max_size):
                operations_needed = 0
                
                for bag_size in nums:
                    operations_needed += (bag_size - 1) // max_size
        
                return operations_needed <= maxOperations

            while left < right:
                mid = (left + right) // 2
                
                if can_reduce_to_max_size(mid):
        
                    right = mid
                else:
        
                    left = mid + 1
            
            return left