class Solution:
    def canChange(self, start: str, target: str) -> bool:
        # First, check if the non-underscore characters are the same
        if start.replace('_', '') != target.replace('_', ''):
            return False
        
        # Two-pointer approach to track piece movements
        n = len(start)
        start_ptr = target_ptr = 0
        
        while start_ptr < n and target_ptr < n:
            # Skip underscore characters in start
            while start_ptr < n and start[start_ptr] == '_':
                start_ptr += 1
            
            # Skip underscore characters in target
            while target_ptr < n and target[target_ptr] == '_':
                target_ptr += 1
            
            # If we've reached the end of either string, break
            if start_ptr == n or target_ptr == n:
                break
            
            # Check movement constraints
            # 'L' can only move left (index should decrease)
            # 'R' can only move right (index should increase)
            if start[start_ptr] == 'L' and start_ptr < target_ptr:
                return False
            
            if start[start_ptr] == 'R' and start_ptr > target_ptr:
                return False
            
            # Move pointers forward
            start_ptr += 1
            target_ptr += 1
        
        return True