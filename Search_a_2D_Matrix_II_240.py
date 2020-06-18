class Solution:
    def searchMatrix(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """
        row_len = len(matrix)
        # col_len = len(matrix[0])

        if not row_len:
            return False

        row = 0
        col = len(matrix[0]) - 1

        while row < row_len and col >= 0:
            val_at_cell = matrix[row][col]
            if val_at_cell == target:
                return True
            elif val_at_cell > target:
                col -= 1
            else:
                row += 1

        return False


obj = Solution()
print("Test Case = matrix: [[1,4,7,11,15],[2,5,8,12,19],[3,6,9,16,22],[10,13,14,17,24],[18,21,23,26,30]], target: 5, Expected result = True, Got result =", obj.searchMatrix(
    [[1, 4, 7, 11, 15], [2, 5, 8, 12, 19], [3, 6, 9, 16, 22], [10, 13, 14, 17, 24], [18, 21, 23, 26, 30]], 5))
print("Test Case = matrix: [[1,4,7,11,15],[2,5,8,12,19],[3,6,9,16,22],[10,13,14,17,24],[18,21,23,26,30]], target: 51, Expected result = False, Got result =", obj.searchMatrix(
    [[1, 4, 7, 11, 15], [2, 5, 8, 12, 19], [3, 6, 9, 16, 22], [10, 13, 14, 17, 24], [18, 21, 23, 26, 30]], 51))
