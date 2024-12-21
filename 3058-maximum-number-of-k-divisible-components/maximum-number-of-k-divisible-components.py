class Solution:
    def maxKDivisibleComponents(self, n: int, edges: List[List[int]], values: List[int], k: int) -> int:
        """
        LeetCode 2872: Find number of components where sum of values is divisible by k
        Time: O(n) where n is number of nodes
        Space: O(n) for adjacency list and visited array
        """
        # Build adjacency list
        adj = [[] for _ in range(n)]
        for u, v in edges:
            adj[u].append(v)
            adj[v].append(u)
        
        self.count = 0
        visited = [False] * n
        
        def dfs(node: int) -> int:
            visited[node] = True
            curr_sum = values[node]
            
            # Process all unvisited neighbors
            for neighbor in adj[node]:
                if not visited[neighbor]:
                    curr_sum += dfs(neighbor)
            
            # If sum is divisible by k, increment count and reset sum
            if curr_sum % k == 0:
                self.count += 1
                return 0
            return curr_sum
        
        dfs(0)
        return self.count