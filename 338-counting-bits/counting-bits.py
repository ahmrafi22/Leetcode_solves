class Solution:
   def countBits(self, n: int) -> List[int]:
           arr=[]
           for i in range(n+1):
               arr.append(bin(i)[2:].count('1'))
           return arr