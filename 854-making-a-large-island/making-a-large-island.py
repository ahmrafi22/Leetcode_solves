class Solution:
    def largestIsland(self, grid: List[List[int]]) -> int:
        n = len(grid)
        
        def paint(i: int, j: int, island_id: int) -> int: # Paint connected 1s with island_id and return size
            if not (0 <= i < n and 0 <= j < n) or grid[i][j] != 1:
                return 0
                
            grid[i][j] = island_id
            size = 1
            # Use tuple for directions to avoid list creation overhead
            for ni, nj in ((i+1,j), (i-1,j), (i,j+1), (i,j-1)):
                size += paint(ni, nj, island_id)
            return size
        
        # Step 1: Label each island with unique ID starting from 2
        # and store their sizes in a dictionary
        island_sizes = {0: 0, 1: 0}  # Initialize with special cases
        island_id = 2
        
        for i in range(n):
            for j in range(n):
                if grid[i][j] == 1:
                    size = paint(i, j, island_id)
                    island_sizes[island_id] = size
                    island_id += 1
        
        # If there's no island, entire grid is 0
        if len(island_sizes) == 2:
            return 1
        
        # If grid is full of 1s
        if len(island_sizes) == 3 and island_sizes[2] == n * n:
            return n * n
        
        # Step 2: Try to connect islands by changing one 0 to 1
        max_size = max(island_sizes.values())  # Initialize with largest existing island
        
        for i in range(n):
            for j in range(n):
                if grid[i][j] == 0:
                    # Use set for O(1) lookup and to avoid counting same island twice
                    neighbor_ids = set()
                    for ni, nj in ((i+1,j), (i-1,j), (i,j+1), (i,j-1)):
                        if 0 <= ni < n and 0 <= nj < n:
                            neighbor_ids.add(grid[ni][nj])
                    
                    # Calculate total size: 1 (for the changed 0) + sum of neighboring island sizes
                    total_size = 1 + sum(island_sizes[nid] for nid in neighbor_ids)
                    max_size = max(max_size, total_size)
        
        return max_size