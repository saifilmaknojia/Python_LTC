from typing import List


class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        if len(grid) < 1:
            return 0

        row = len(grid)
        col = len(grid[0])

        for r in range(1, col):
            grid[0][r] += grid[0][r - 1]

        for c in range(1, row):
            grid[c][0] += grid[c - 1][0]

        for i in range(1, row):
            for j in range(1, col):
                grid[i][j] += min(grid[i-1][j], grid[i][j-1])

        return grid[row - 1][col - 1]


obj = Solution()
print("Test case 1: [[1,3,1],[1,5,11],[4,2,1]], Expected result = 9, Got result =",
      obj.minPathSum([[1, 3, 1], [1, 5, 6], [4, 2, 1]]))
print("Test case 2: [[1,2,5],[3,2,1]], Expected result = 6, Got result =",
      obj.minPathSum([[1, 2, 5], [3, 2, 1]]))
