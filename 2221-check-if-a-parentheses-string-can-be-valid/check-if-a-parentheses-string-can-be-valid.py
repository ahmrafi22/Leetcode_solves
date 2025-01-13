class Solution:
    def canBeValid(self, s: str, locked: str) -> bool:
        if len(s) % 2:
            return False
            
        # Check if we have enough opening parentheses
        unlocked = 0
        open_count = 0
        
        for i in range(len(s)):
            if locked[i] == '0':
                unlocked += 1
            elif s[i] == '(':
                open_count += 1
            else:
                open_count -= 1
                
            if open_count + unlocked < 0:
                return False
        
        # Check if we have enough closing parentheses
        unlocked = 0
        close_count = 0
        
        for i in range(len(s) - 1, -1, -1):
            if locked[i] == '0':
                unlocked += 1
            elif s[i] == ')':
                close_count += 1
            else:
                close_count -= 1
                
            if close_count + unlocked < 0:
                return False
                
        return True