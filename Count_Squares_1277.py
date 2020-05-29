from typing import List


class Solution:
    def countSquares(self, matrix: List[List[int]]) -> int:
        # idea is same as maximal square in a matrix
        result = 0
        row = len(matrix)
        col = len(matrix[0])
        for i in range(row):
            for j in range(col):
                if matrix[i][j] > 0 and i > 0 and j > 0:
                    min_3_directions = min(
                        matrix[i-1][j], matrix[i][j-1], matrix[i-1][j-1])
                    # print("i = ", i, " j = ", j, " min = ", min_3_directions)
                    matrix[i][j] += min_3_directions

                result += matrix[i][j]

        return result
