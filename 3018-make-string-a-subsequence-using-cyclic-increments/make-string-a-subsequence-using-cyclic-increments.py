class Solution:
    def canMakeSubsequence(self, str1: str, str2: str) -> bool:
        # Two-pointer approach
        # i points to str1, j points to str2
        i, j = 0, 0
        
        while i < len(str1) and j < len(str2):
            # Check if current character in str1 matches str2 directly
            # Or if incrementing str1's character cyclically matches str2
            if str1[i] == str2[j] or chr((ord(str1[i]) - ord('a') + 1) % 26 + ord('a')) == str2[j]:
                j += 1  # Move to next character in str2
            
            i += 1  # Always move to next character in str1
        
        # If we've matched all characters in str2, return True
        return j == len(str2)