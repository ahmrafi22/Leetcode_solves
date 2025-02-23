# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def constructFromPrePost(self, pre: List[int], post: List[int]) -> Optional[TreeNode]:
        def build(i: int, j: int, n: int) -> Optional[TreeNode]:
            if n <= 0: return None
            root = TreeNode(pre[i])
            if n == 1: return root
            
            for k in range(n):
                if post[j + k] == pre[i + 1]:
                    break
                    
            size = k + 1
            root.left = build(i + 1, j, size)
            root.right = build(i + 1 + size, j + size, n - 1 - size)
            return root
            
        return build(0, 0, len(pre))