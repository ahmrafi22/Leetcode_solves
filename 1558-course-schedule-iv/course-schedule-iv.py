from collections import defaultdict, deque
from typing import List

class Solution:
    def checkIfPrerequisite(self, numCourses: int, prerequisites: List[List[int]], queries: List[List[int]]) -> List[bool]:
        # Create adjacency list representation
        adj = defaultdict(list)
        for pre, course in prerequisites:
            adj[course].append(pre)
        
        # Create reachability matrix
        reachable = [[False] * numCourses for _ in range(numCourses)]
        
        # Run BFS from each course
        for course in range(numCourses):
            visited = [False] * numCourses
            queue = deque([course])
            visited[course] = True
            
            while queue:
                node = queue.popleft()
                # Check all prerequisites of current node
                for prereq in adj[node]:
                    if not visited[prereq]:
                        visited[prereq] = True
                        reachable[prereq][course] = True
                        queue.append(prereq)
        
        # Answer queries using the reachability matrix
        return [reachable[course][target] for course, target in queries]