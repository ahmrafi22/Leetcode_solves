class Solution:
    def isPrefixAndSuffix(self, s1: str, s2: str) -> bool:
       
        n = len(s1)
        return s2.startswith(s1) and s2.endswith(s1)
    
    def countPrefixSuffixPairs(self, words: list[str]) -> int:
        n = len(words)
        ans = 0
        
        
        lengths = [len(w) for w in words]
        
        for i in range(n - 1):
            len_i = lengths[i]
            word_i = words[i]
            
            
            ans += sum(
                1 
                for j in range(i + 1, n)
                if lengths[j] >= len_i and self.isPrefixAndSuffix(word_i, words[j])
            )
            
        return ans