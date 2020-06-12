from typing import List
import math


class Solution:
    def updateMatrix(self, matrix: List[List[int]]) -> List[List[int]]:
        # Two steps DP
        # First take minimum of left and top by moving from top left to bottom right
        # then take minimum of bottom and right by moving from bottom right to top left

        row = len(matrix)
        col = len(matrix[0])
        result = [[0 for _ in range(col)] for _ in range(row)]

        for i in range(0, row):
            for j in range(0, col):

                if matrix[i][j] == 1:
                    left = math.inf
                    top = math.inf
                    if i > 0:
                        top = result[i-1][j]
                    if j > 0:
                        left = result[i][j-1]

                    result[i][j] = matrix[i][j] + min(top, left)

        # moving from bottom right to top left
        # take minimum of bottom and right by
        # print(result)
        for i in range(row - 1, -1, -1):
            for j in range(col - 1, -1, -1):
                if matrix[i][j] == 1:
                    right = math.inf
                    bottom = math.inf

                    if i < row-1:
                        bottom = result[i+1][j]
                    if j < col - 1:
                        right = result[i][j+1]

                    result[i][j] = min(result[i][j], matrix[i]
                                       [j] + min(bottom, right))

        return result


obj = Solution()
print("Test Case: [[0,0,0], [0,1,0], [1,1,1]], Expected result = [[0,0,0],[0,1,0],[1,2,1]], Got result =",
      obj.updateMatrix([[0, 0, 0], [0, 1, 0], [1, 1, 1]]))
