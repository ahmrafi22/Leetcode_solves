class Solution:
    def eventualSafeNodes(self, graph: List[List[int]]) -> List[int]:
        n = len(graph)
        # 0: unvisited, 1: visiting, 2: safe, 3: unsafe
        state = [0] * n
        
        def dfs(node):
            # If we've already determined the state of this node, return it
            if state[node] != 0:
                return state[node] == 2
            
            # Mark as currently visiting
            state[node] = 1
            
            # Check all neighboring nodes
            for neighbor in graph[node]:
                # If any neighbor is unsafe or part of a cycle, this node is unsafe
                if state[neighbor] == 1 or not dfs(neighbor):
                    state[node] = 3
                    return False
            
            # If we've reached here, the node is safe
            state[node] = 2
            return True
        
        # Run DFS on each unvisited node
        for i in range(n):
            if state[i] == 0:
                dfs(i)
        
        # Collect all safe nodes
        return [i for i in range(n) if state[i] == 2]