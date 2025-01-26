class Solution:
    def maximumInvitations(self, favorite: List[int]) -> int:
        # Find the maximum invitations by comparing cycle size and mutual chain length
        return max(self.find_max_cycle(favorite), self.calculate_mutual_chains(favorite))
    
    def find_max_cycle(self, favorite):
        n = len(favorite)
        visited = [False] * n
        max_cycle_size = 0
        
        for start in range(n):
            if visited[start]:
                continue
            
            # Keep track of nodes in current path and their positions
            path = []
            path_set = set()
            current = start
            
            # Detect cycle
            while current not in path_set:
                if visited[current]:
                    break
                
                path.append(current)
                path_set.add(current)
                visited[current] = True
                current = favorite[current]
            
            # If a cycle is found
            if current in path_set:
                cycle_start = path.index(current)
                cycle_length = len(path) - cycle_start
                max_cycle_size = max(max_cycle_size, cycle_length)
        
        return max_cycle_size
    
    def calculate_mutual_chains(self, favorite):
        n = len(favorite)
        indegree = [0] * n
        for f in favorite:
            indegree[f] += 1
        
        # Compute chain lengths
        chain_length = [1] * n
        queue = [i for i in range(n) if indegree[i] == 0]
        
        while queue:
            current = queue.pop()
            next_node = favorite[current]
            chain_length[next_node] = max(chain_length[next_node], chain_length[current] + 1)
            
            indegree[next_node] -= 1
            if indegree[next_node] == 0:
                queue.append(next_node)
        
        # Find total chain length for mutual pairs
        total_chain_length = 0
        for i in range(n):
            if i == favorite[favorite[i]]:
                total_chain_length += chain_length[i]
        
        return total_chain_length