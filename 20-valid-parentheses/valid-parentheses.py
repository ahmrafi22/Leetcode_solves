class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        pairs = {')': '(', '}': '{', ']': '['}
        
        for char in s:
            if char not in pairs:  # Opening bracket
                stack.append(char)
            elif not stack or stack.pop() != pairs[char]:  # Closing bracket
                return False
                
        return len(stack) == 0