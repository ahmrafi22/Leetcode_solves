class Solution:
   def clearDigits(self, s: str) -> str:
       result = []
       for char in s:
           if char.isdigit():
               result.pop() if result else None
           else:
               result.append(char)
       return ''.join(result)