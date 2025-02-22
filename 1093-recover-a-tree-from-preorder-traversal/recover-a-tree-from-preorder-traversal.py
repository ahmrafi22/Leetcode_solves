# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def recoverFromPreorder(self, data: str) -> Optional[TreeNode]:
        if not data: return None
        for i in range(100, 0, -1):
            data = data.replace("-" * i, chr(i + 65))
            
        def build_tree(parts: str, level: int) -> Optional[TreeNode]:
            if not parts: return None
            parts = parts.split(chr(level + 65))
            node = TreeNode(int(parts[0]))
            node.left = build_tree(parts[1], level + 1) if len(parts) > 1 else None
            node.right = build_tree(parts[2], level + 1) if len(parts) > 2 else None
            return node
            
        return build_tree(data, 1)