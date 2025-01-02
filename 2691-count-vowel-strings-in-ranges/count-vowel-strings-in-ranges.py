class Solution:
   def isVowel(self, c: str) -> bool:
       return c in 'aeiou'
       
   def vowelStrings(self, words: List[str], queries: List[List[int]]) -> List[int]:
       # Mark words starting and ending with vowels
       v = [1 if self.isVowel(word[0]) and self.isVowel(word[-1]) else 0 for word in words]
       
       # Build prefix sum array
       prefix = [v[0]] + [0] * (len(v)-1)
       for i in range(1, len(v)):
           prefix[i] = prefix[i-1] + v[i]
           
       # Process queries
       return [prefix[r] if l == 0 else prefix[r] - prefix[l-1] for l, r in queries]