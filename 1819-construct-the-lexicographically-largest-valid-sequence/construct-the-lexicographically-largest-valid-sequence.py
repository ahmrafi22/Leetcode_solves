class Solution:
   def constructDistancedSequence(self, n: int) -> list[int]:
       seq = [0] * (2 * n - 1)
       used = [False] * (n + 1)
       
       def backtrack(pos: int) -> bool:
           if pos == len(seq): return True
           if seq[pos]: return backtrack(pos + 1)
           
           for num in range(n, 0, -1):
               if used[num] or (num > 1 and (pos + num >= len(seq) or seq[pos + num])): continue
               used[num] = True
               seq[pos] = num
               if num > 1: seq[pos + num] = num
               if backtrack(pos + 1): return True
               used[num] = False
               seq[pos] = 0
               if num > 1: seq[pos + num] = 0
                   
           return False
           
       backtrack(0)
       return seq