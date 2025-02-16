class Solution:
   def punishmentNumber(self, n: int) -> int:
       def canPartition(s: str, target: int, start: int, curr_sum: int) -> bool:
           if start == len(s):
               return curr_sum == target
           
           num = 0
           for i in range(start, len(s)):
               num = num * 10 + int(s[i])
               if curr_sum + num > target:
                   break
               if canPartition(s, target, i + 1, curr_sum + num):
                   return True
           return False

       def isPunishmentNumber(i: int) -> bool:
           return canPartition(str(i * i), i, 0, 0)

       result = 0
       for i in range(1, n + 1):
           if isPunishmentNumber(i):
               result += i * i
       return result