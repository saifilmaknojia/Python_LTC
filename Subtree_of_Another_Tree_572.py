# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def isSubtree(self, s: TreeNode, t: TreeNode) -> bool:
        # if s is null, return false
        if not s:
            return False

        return (s.val == t.val and self.checkSubTree(s, t)) or self.isSubtree(s.left, t) or self.isSubtree(s.right, t)

    def checkSubTree(self, tree_s, tree_t):
        # if s and t both are null, return true
        if not tree_s and not tree_t:
            return True

        # if either s or t is null, return false
        if not tree_s or not tree_t:
            return False

        return tree_s.val == tree_t.val and self.checkSubTree(tree_s.left, tree_t.left) and self.checkSubTree(tree_s.right, tree_t.right)
