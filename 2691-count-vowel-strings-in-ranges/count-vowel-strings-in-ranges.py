class Solution:
    def vowelStrings(self, words: List[str], queries: List[List[int]]) -> List[int]:
        # Dictionary to mark words that start and end with vowels
        mp = {}
        vowels = set('aeiou')
        
        # Check each word and mark if it starts and ends with vowel
        for i in range(len(words)):
            if words[i][0] in vowels and words[i][-1] in vowels:
                mp[i] = 1
        
        # Create prefix sum array
        prefix = [0] * len(words)
        prefix[0] = mp.get(0, 0)  # Handle case when first word doesn't start/end with vowels
        
        # Build prefix sum array
        for i in range(1, len(words)):
            prefix[i] = prefix[i-1] + mp.get(i, 0)
        
        # Process queries
        ans = []
        for left, right in queries:
            if left == 0:
                ans.append(prefix[right])
            else:
                ans.append(prefix[right] - prefix[left-1])
                
        return ans