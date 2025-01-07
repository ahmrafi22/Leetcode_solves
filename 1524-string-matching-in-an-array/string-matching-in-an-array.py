class Solution:
    def stringMatching(self, words: List[str]) -> List[str]:
        # Create a set to store unique matching substrings
        uans = set()
        
        # Sort words by length
        words.sort(key=len)
        
        # Check each word against the longer words
        for i in range(len(words)):
            for j in range(i + 1, len(words)):
                if words[i] in words[j]:
                    uans.add(words[i])
                    break  # No need to check further if we've found a match
        
        return list(uans)

