from typing import List


class Solution:
    def generateMatrix(self, n: int) -> List[List[int]]:
        matrix = [[0 for col in range(n)] for row in range(n)]

        top = left = 0
        bottom = right = n-1
        counter = 1
        while top <= bottom and left <= right:

            # fill by moving top left to top right
            for i in range(left, right + 1):
                matrix[top][i] = counter
                counter += 1
            top += 1

            # print(matrix)
            # fill by moving top right to bottom right
            for i in range(top, bottom + 1):
                matrix[i][right] = counter
                counter += 1
            right -= 1

            # fill by moving bottom right to bottom left
            for i in range(right, left-1, -1):
                matrix[bottom][i] = counter
                counter += 1
            bottom -= 1

            for i in range(bottom, top-1, -1):
                matrix[i][left] = counter
                counter += 1
            left += 1

        return matrix


obj = Solution()
print(
    "Test case: n = 3, Expected result = [[1,2,3],[8,9,4],[7,6,5]], Got result =", obj.generateMatrix(3))
print(
    "Test case: n = 5, Expected result = [[1,2,3,4,5],[16,17,18,19,6],[15,24,25,20,7],[14,23,22,21,8],[13,12,11,10,9]], Got result =", obj.generateMatrix(5))
