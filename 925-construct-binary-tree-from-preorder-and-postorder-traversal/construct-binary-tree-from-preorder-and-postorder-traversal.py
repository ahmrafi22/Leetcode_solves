# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def constructFromPrePost(self, pre: List[int], post: List[int]) -> Optional[TreeNode]:
        # Create index map for O(1) lookups
        post_idx = {val: idx for idx, val in enumerate(post)}
        n = len(pre)
        
        def build(pre_l: int, pre_r: int, post_l: int, post_r: int) -> Optional[TreeNode]:
            # Base cases
            if pre_l > pre_r or post_l > post_r:
                return None
            if pre_l == pre_r:
                return TreeNode(pre[pre_l])
            
            root = TreeNode(pre[pre_l])
            
            # Get left child from preorder and find its position in postorder
            left_val = pre[pre_l + 1]
            left_idx_post = post_idx[left_val]
            
            # Calculate size of left subtree
            left_size = left_idx_post - post_l + 1
            
            # Recursively build left and right subtrees with correct bounds
            root.left = build(
                pre_l + 1,                # left subtree start in preorder
                pre_l + left_size,        # left subtree end in preorder
                post_l,                   # left subtree start in postorder
                left_idx_post            # left subtree end in postorder
            )
            
            root.right = build(
                pre_l + left_size + 1,    # right subtree start in preorder
                pre_r,                    # right subtree end in preorder
                left_idx_post + 1,        # right subtree start in postorder
                post_r - 1               # right subtree end in postorder
            )
            
            return root
        
        return build(0, n-1, 0, n-1) if n else None