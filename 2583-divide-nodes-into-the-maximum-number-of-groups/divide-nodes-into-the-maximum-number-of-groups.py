from collections import deque, defaultdict

class Solution:
    def magnificentSets(self, n: int, edges: List[List[int]]) -> int:
        graph = [[] for _ in range(n + 1)]
        for a, b in edges:
            graph[a].append(b)
            graph[b].append(a)
        
        def bfs(start): # maximum possible groups from this starting node"
            queue = deque([(start, 1)])  # (node, group number)
            visited = {start: 1}  # node -> group number
            max_level = 1
            
            while queue:
                node, level = queue.popleft()
                for nei in graph[node]:
                    if nei not in visited:
                        visited[nei] = level + 1
                        queue.append((nei, level + 1))
                        max_level = max(max_level, level + 1)
                    elif abs(visited[nei] - level) != 1:
                        return 0
            return max_level
        
        def find_component(node, visited, component): # Find all nodes in the same component
            queue = deque([node])
            while queue:
                curr = queue.popleft()
                if curr not in visited:
                    visited.add(curr)
                    component.append(curr)
                    queue.extend(graph[curr])
        
        visited = set()
        total_groups = 0
        
        # Process each connected component
        for node in range(1, n + 1):
            if node not in visited:
                component = []
                find_component(node, visited, component)
                
                # starting from each node in component
                max_groups = 0
                for start in component:
                    groups = bfs(start)
                    if groups == 0:  # If impossible
                        return -1
                    max_groups = max(max_groups, groups)
                
                total_groups += max_groups
        
        return total_groups