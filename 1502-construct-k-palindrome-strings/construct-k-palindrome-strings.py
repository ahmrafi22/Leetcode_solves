class Solution:
    def canConstruct(self, s: str, k: int) -> bool:
        if len(s) < k:
            return False
        if len(s) == k:
            return True
            
        odd_mask = 0
        for char in s:
            odd_mask ^= (1 << (ord(char) - ord('a')))
            
        return bin(odd_mask).count('1') <= k