# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def maximumAverageSubtree(self, root: TreeNode) -> float:
        self.result = 0
        self.calculateDFS(root, [0, 0])
        return self.result

    def calculateDFS(self, r, arr):
        """ arr[0] = sum of subtrees, arr[1] = count of nodes in subtrees """
        if not r:
            return [0, 0]

        left = self.calculateDFS(r.left, arr)
        right = self.calculateDFS(r.right, arr)

        total_sum = left[0] + right[0] + r.val
        total_nodes = left[1] + right[1] + 1

        avg = total_sum / total_nodes
        self.result = max(self.result, avg)

        return [total_sum, total_nodes]
