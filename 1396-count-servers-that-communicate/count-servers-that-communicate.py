class Solution:
    def countServers(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        row = [0] * m
        col = [0] * n
        
        # Count servers in rows and columns
        for i in range(m):
            for j in range(n):
                if grid[i][j]:
                    row[i] += 1
                    col[j] += 1
        
        # Count communicating servers
        return sum(grid[i][j] for i in range(m) for j in range(n) 
                   if grid[i][j] and (row[i] > 1 or col[j] > 1))