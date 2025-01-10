from collections import Counter
from typing import List

class Solution:
    def wordSubsets(self, words1: List[str], words2: List[str]) -> List[str]:
        max_freq = Counter()
        for word in words2:
            word_freq = Counter(word)
            for char, count in word_freq.items():
                max_freq[char] = max(max_freq[char], count)
    
        def is_subset(word: str) -> bool:
            word_freq = Counter(word)
            return all(word_freq[char] >= count for char, count in max_freq.items())

        return [word for word in words1 if is_subset(word)]