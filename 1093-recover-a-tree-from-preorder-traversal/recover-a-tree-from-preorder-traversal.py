# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def recoverFromPreorder(self, traversal: str) -> Optional[TreeNode]:
        if not traversal:
            return None
            
        # Stack to keep track of nodes at different levels
        stack = []
        i = 0
        
        while i < len(traversal):
            # Count the number of dashes to determine level
            level = 0
            while i < len(traversal) and traversal[i] == '-':
                level += 1
                i += 1
            
            # Get the node value
            value = 0
            while i < len(traversal) and traversal[i].isdigit():
                value = value * 10 + int(traversal[i])
                i += 1
            
            # Create new node
            node = TreeNode(value)
            
            # Pop nodes from stack if current level is less than stack size
            while len(stack) > level:
                stack.pop()
            
            # Connect the node to its parent
            if stack:
                if not stack[-1].left:
                    stack[-1].left = node
                else:
                    stack[-1].right = node
            
            stack.append(node)
        
        # Return the root node (first node in the traversal)
        return stack[0]