class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        chars = {}
        for char in magazine:
            if char not in chars: 
                chars[char] = 1
            else: 
                chars[char] += 1
        
        for char in ransomNote:
            if char in chars and chars[char] > 0:
                chars[char] -= 1
            else:
                return False
        
        return True