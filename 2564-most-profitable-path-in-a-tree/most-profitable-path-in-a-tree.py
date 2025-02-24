class Solution:
    def mostProfitablePath(self, edges, bob, amount):
        n = len(amount)
        graph = [[] for _ in range(n)]
        for u, v in edges:
            graph[u].append(v)
            graph[v].append(u)
        
        bob_time_to_node = [-1] * n
        
        def find_bob_path(node, parent, time):
            if node == 0:
                bob_time_to_node[node] = time
                return True
                
            for neighbor in graph[node]:
                if neighbor != parent:
                    if find_bob_path(neighbor, node, time + 1):
                        bob_time_to_node[node] = time
                        return True
            return False
        
        find_bob_path(bob, -1, 0)
        
        def alice_dfs(node, parent, time, score):
            curr_score = score
            
            if bob_time_to_node[node] == -1 or time < bob_time_to_node[node]:
                curr_score += amount[node]
            elif time == bob_time_to_node[node]:
                curr_score += amount[node] // 2
            
            is_leaf = node != 0 and len(graph[node]) == 1
            if is_leaf:
                return curr_score
            
            max_score = float('-inf')
            for neighbor in graph[node]:
                if neighbor != parent:
                    max_score = max(max_score, alice_dfs(neighbor, node, time + 1, curr_score))
            
            return max_score
        
        return alice_dfs(0, -1, 0, 0)