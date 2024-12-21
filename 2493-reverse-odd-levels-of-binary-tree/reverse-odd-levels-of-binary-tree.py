# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def reverseOddLevels(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if not root:
            return None
            
        def reverse_nodes(left: Optional[TreeNode], right: Optional[TreeNode], level: int = 0) -> None:
            if not left or not right:
                return
                
            if level % 2 == 1:
                left.val, right.val = right.val, left.val
                
            reverse_nodes(left.left, right.right, level + 1)
            reverse_nodes(left.right, right.left, level + 1)
            
        if root.left:
            reverse_nodes(root.left, root.right, 1)
            
        return root
        