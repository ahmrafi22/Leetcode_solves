class Solution:
    def shiftingLetters(self, s: str, shifts: list[list[int]]) -> str:
        n = len(s)
        # Initialize difference array
        apply = [0] * (n + 1)
        
        # Process all shifts using difference array technique
        for start, end, direction in shifts:
            d = 1 if direction == 1 else -1
            apply[start] += d
            apply[end + 1] -= d
        
        # Calculate prefix sum
        for i in range(1, n + 1):
            apply[i] += apply[i - 1]
        
        # Convert string to list for efficient character manipulation
        result = list(s)
        
        # Apply shifts to each character
        for i in range(n):
            # Calculate new character position
            new_pos = (ord(result[i]) - ord('a') + apply[i]) % 26
            result[i] = chr(ord('a') + new_pos)
        
        return ''.join(result)