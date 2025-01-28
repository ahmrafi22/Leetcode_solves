class Solution:
    def findMaxFish(self, grid: List[List[int]]) -> int:
        if not grid or not grid[0]:
            return 0
            
        m, n = len(grid), len(grid[0])
        max_fish = 0
        
        def dfs(i: int, j: int) -> int:
            # Check bounds and if cell has already been visited (0)
            if i < 0 or i >= m or j < 0 or j >= n or grid[i][j] == 0:
                return 0
                
            # Store current cell's fish count and mark as visited
            fish = grid[i][j]
            grid[i][j] = 0  # Mark as visited by setting to 0
            
            # Explore all 4 directions and accumulate fish count
            directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]
            for di, dj in directions:
                fish += dfs(i + di, j + dj)
                
            return fish
        
        # Try starting DFS from each non-zero cell
        for i in range(m):
            for j in range(n):
                if grid[i][j]:  # If cell contains fish
                    max_fish = max(max_fish, dfs(i, j))
        
        return max_fish