from typing import List
from collections import deque
# Definition for a binary tree node.


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def levelOrderBottom(self, root: TreeNode) -> List[List[int]]:
        def dfs(r, level):
            if not r:
                return

            nonlocal result_list
            if level == len(result_list):
                result_list.append([])

            result_list[level].append(r.val)
          #  print(result_list)
            dfs(r.left, level + 1)
            dfs(r.right, level + 1)

            return

        result_list = []
        dfs(root, 0)
        ans = deque([])

        for result in result_list:
            ans.appendleft(result)

        return ans
