class Solution:
    def reverseVowels(self, s: str) -> str:
        vowels = []
        for i in s:
            if i in 'aeiouAEIOU':
                vowels.append(i)
        
        s = list(s)
        for idx in range(len(s)):
            if s[idx] in 'aeiouAEIOU':
                s[idx] = vowels.pop()
        
        return ''.join(s)