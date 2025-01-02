class Solution:
   def valid(self, s: str) -> bool:
       vowels = set('aeiou')
       return s[0] in vowels and s[-1] in vowels
       
   def vowelStrings(self, words: List[str], queries: List[List[int]]) -> List[int]:
       n = len(words)
       prefix = [0] * n
       prefix[0] = 1 if self.valid(words[0]) else 0
       
       for i in range(1, n):
           prefix[i] = prefix[i-1] + (1 if self.valid(words[i]) else 0)
           
       return [prefix[q[1]] if q[0] == 0 else prefix[q[1]] - prefix[q[0]-1] for q in queries]