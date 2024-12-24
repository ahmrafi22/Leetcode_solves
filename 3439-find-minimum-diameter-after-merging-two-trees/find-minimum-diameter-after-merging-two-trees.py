class Solution:
    def minimumDiameterAfterMerge(self, edges1: list[list[int]], edges2: list[list[int]]) -> int:
        # Initialize variables
        n1 = len(edges1) + 1
        n2 = len(edges2) + 1
        graph1 = [[] for _ in range(n1)]
        graph2 = [[] for _ in range(n2)]
        
        # Build adjacency lists for both graphs
        for edge in edges1:
            graph1[edge[0]].append(edge[1])
            graph1[edge[1]].append(edge[0])
        for edge in edges2:
            graph2[edge[0]].append(edge[1])
            graph2[edge[1]].append(edge[0])
        
        # Calculate diameter of first graph
        self.dia = -1
        visited1 = [False] * n1
        self.getDia(0, graph1, visited1)
        d1 = self.dia
        
        # Calculate diameter of second graph
        self.dia = -1
        visited2 = [False] * n2
        self.getDia(0, graph2, visited2)
        d2 = self.dia
        
        # Calculate minimum possible diameter after merging
        cand = (d1 + 1) // 2 + (d2 + 1) // 2 + 1
        return max(cand, max(d1, d2))
    
    def getDia(self, src: int, graph: list[list[int]], visited: list[bool]) -> int:
        visited[src] = True
        dch = -1  # deepest child
        sdch = -1  # second deepest child
        
        # Explore all unvisited children
        for child in graph[src]:
            if not visited[child]:
                ch = self.getDia(child, graph, visited)
                if ch > dch:
                    sdch = dch
                    dch = ch
                elif ch > sdch:
                    sdch = ch
        
        # Update diameter if path through current node is longer
        if dch + sdch + 2 > self.dia:
            self.dia = dch + sdch + 2
            
        return dch + 1
        