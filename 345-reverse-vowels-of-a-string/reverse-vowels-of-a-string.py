class Solution:
    def reverseVowels(self, s: str) -> str:
        vowels = []
        for i in s:
            if i in 'aeiouAEIOU':
                vowels.append(i)
        
        vowels.reverse()
        
        s = list(s)
        j = 0
        for idx in range(len(s)):
            if s[idx] in 'aeiouAEIOU':
                s[idx] = vowels[j]
                j += 1
        
        return ''.join(s)