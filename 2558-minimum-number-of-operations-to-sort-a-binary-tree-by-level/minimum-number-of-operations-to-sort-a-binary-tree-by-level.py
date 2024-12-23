# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

from collections import deque
from typing import List, Optional

class Solution:
    def minSwaps(self, arr: List[int], n: int) -> int:
        # Create array of value-index pairs
        arr_pos = [(arr[i], i) for i in range(n)]
        arr_pos.sort()
        
        vis = [False] * n
        ans = 0
        
        for i in range(n):
            if vis[i] or arr_pos[i][1] == i:
                continue
                
            cycle_size = 0
            j = i
            while not vis[j]:
                vis[j] = True
                j = arr_pos[j][1]
                cycle_size += 1
                
            if cycle_size > 0:
                ans += (cycle_size - 1)
                
        return ans
    
    def minimumOperations(self, root: Optional[TreeNode]) -> int:
        q = deque([root])
        ans = 0
        
        while q:
            level = []
            size = len(q)
            
            for _ in range(size):
                temp = q.popleft()
                level.append(temp.val)
                
                if temp.left:
                    q.append(temp.left)
                if temp.right:
                    q.append(temp.right)
            
            ans += self.minSwaps(level, len(level))
            
        return ans