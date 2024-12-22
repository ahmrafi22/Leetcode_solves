from typing import List
import heapq

class Solution:
    def leftmostBuildingQueries(self, heights: List[int], queries: List[List[int]]) -> List[int]:
        """
        Find the leftmost building that is taller than both buildings in each query.
        
        For each query [a, b], finds the smallest index i where:
        - i >= max(a, b)
        - heights[i] > heights[a] and heights[i] > heights[b]
        
        Args:
            heights: List of building heights
            queries: List of pairs [a, b] representing queries
            
        Returns:
            List of indices where each index is the answer for corresponding query.
            Returns -1 if no such building exists for a query.
        
        Time Complexity: O(n + q * log q) where n = len(heights), q = len(queries)
        Space Complexity: O(q) for the deferred queries and priority queue
        """
        n, q = len(heights), len(queries)
        result = [-1] * q
        # Store (required_height, query_index) for each building index
        deferred = [[] for _ in range(n)]
        
        # Process each query
        for i, (a, b) in enumerate(queries):
            # Normalize query so a <= b
            if a > b:
                a, b = b, a
                
            # Case 1: Same building or right building is taller
            if a == b or heights[a] < heights[b]:
                result[i] = b
                continue
                
            # Case 2: Need to find a taller building
            # Store the required height (max of both buildings) and query index
            required_height = max(heights[a], heights[b])
            deferred[b].append((required_height, i))
        
        # Min heap to track pending queries by required height
        pq = []
        
        # Process buildings from left to right
        for i in range(n):
            # Add new queries that start from current building
            for required_height, query_idx in deferred[i]:
                heapq.heappush(pq, (required_height, query_idx))
            
            # Process queries that can be answered by current building
            current_height = heights[i]
            while pq and pq[0][0] < current_height:
                _, query_idx = heapq.heappop(pq)
                result[query_idx] = i
        
        return result

    def validate_input(self, heights: List[int], queries: List[List[int]]) -> None:
        """
        Validates input parameters.
        
        Raises:
            ValueError: If input constraints are violated
        """
        if not heights or not queries:
            raise ValueError("Heights and queries cannot be empty")
            
        if any(len(q) != 2 for q in queries):
            raise ValueError("Each query must contain exactly 2 indices")
            
        n = len(heights)
        if any(not (0 <= a < n and 0 <= b < n) for a, b in queries):
            raise ValueError("Query indices must be within valid range")