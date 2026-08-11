# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        if not subRoot:
            return True

        if not root:
            return False

        # Check if the trees match starting at this node
        if self.sameTree(root, subRoot):
            return True

        # Otherwise search the left and right side
        return (
            self.isSubtree(root.left, subRoot)
            or
            self.isSubtree(root.right, subRoot)
        )


    def sameTree(
        self,
        root: Optional[TreeNode],
        subRoot: Optional[TreeNode]
    ) -> bool:

        # Both are empty
        if not root and not subRoot:
            return True

        # One is empty but the other isn't
        if not root or not subRoot:
            return False

        # Values don't match
        if root.val != subRoot.val:
            return False

        # Left sides AND right sides must match
        return (
            self.sameTree(root.left, subRoot.left)
            and
            self.sameTree(root.right, subRoot.right)
        )