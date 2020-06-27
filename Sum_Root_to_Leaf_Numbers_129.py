# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def sumNumbers(self, root: TreeNode) -> int:

        def sum_root_to_leaf(r, total):
            if not r:
                return 0
            total = (total * 10) + r.val
            if not r.left and not r.right:
                return total
            # print(total)
            left = sum_root_to_leaf(r.left, total)
            right = sum_root_to_leaf(r.right, total)

            # print(left, right)
            return left + right

        return sum_root_to_leaf(root, 0)
