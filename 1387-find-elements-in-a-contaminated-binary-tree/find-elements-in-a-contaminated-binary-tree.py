# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class FindElements:

    def __init__(self, root: Optional[TreeNode]):
        self.root=root
        self.a=set()
        self.recover(root,0)
        
    def recover(self,node,value):
        self.a.add(value)
        node.val=value
        if node.left:
            self.recover(node.left,2*value+1)
        if node.right:
            self.recover(node.right,2*value+2)
    def find(self, target: int) -> bool:
        return target in self.a


# Your FindElements object will be instantiated and called as such:
# obj = FindElements(root)
# param_1 = obj.find(target)