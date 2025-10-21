class Solution:
    def stringMatching(self, words: List[str]) -> List[str]:
        combined = " ".join(words)
        return [w for w in words if combined.count(w) >= 2]