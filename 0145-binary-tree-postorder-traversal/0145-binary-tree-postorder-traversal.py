# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        result = []
        
        def traverse(node):
            if node is None:
                return
            traverse(node.left)   # Visit left subtree
            traverse(node.right)  # Visit right subtree
            result.append(node.val)  # Visit root node
        
        traverse(root)
        return result        