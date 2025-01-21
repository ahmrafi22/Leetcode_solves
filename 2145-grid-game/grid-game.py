import itertools
class Solution:
    def gridGame(self, grid: List[List[int]]) -> int:
         upper, lower = grid
         upper_total = sum(upper)
         upper_cum = list(itertools.accumulate(upper))
         lower_cum = list(itertools.accumulate(lower))
    
         min_score = float('inf')
         for i in range(len(upper)):
             robot1_path = upper_total - upper_cum[i]
             robot2_path = lower_cum[i-1] if i > 0 else 0
             min_score = min(min_score, max(robot1_path, robot2_path))
    
         return min_score
        