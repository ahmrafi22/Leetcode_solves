# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class FindElements:
    def __init__(self, root: Optional[TreeNode]):
        self.root = root

    def find(self, target: int) -> bool:
        if target == 0:
            return self.root is not None
        
        path = target + 1
        depth = path.bit_length() - 1
        node = self.root
        mask = 1 << (depth - 1)
        while mask > 0 and node is not None:
            node = node.left if (path & mask) == 0 else node.right    
            mask >>= 1
        
        return node is not None
        


# Your FindElements object will be instantiated and called as such:
# obj = FindElements(root)
# param_1 = obj.find(target)