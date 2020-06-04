from collections import deque


class TreeNode:
    """ Definition for a binary tree node. """

    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def invertTree(self, root: TreeNode) -> TreeNode:
        if root is None:
            return None

        left = self.invertTree(root.left)
        right = self.invertTree(root.right)

        root.left = right
        root.right = left

        return root

    def invertTree_BFS(self, root: TreeNode) -> TreeNode:
        if root is None:
            return root

        queue = deque()
        queue.append(root)

        while queue:
            pop = queue.popleft()

            temp = pop.left
            pop.left = pop.right
            pop.right = temp

            if pop.left:
                queue.append(pop.left)
            if pop.right:
                queue.append(pop.right)

        return root
