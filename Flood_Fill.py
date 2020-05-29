from typing import List


class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, newColor: int) -> List[List[int]]:
        if image[sr][sc] == newColor:
            return image

        directions = [[1, 0], [-1, 0], [0, 1], [0, -1]]

        old_color = image[sr][sc]
        row_len = len(image)
        col_len = len(image[0])

        def dfsColor(row, col):
            image[row][col] = newColor
            for r, c in directions:
                new_r = row + r
                new_c = col + c

            if new_r >= 0 and new_r < row_len and new_c >= 0 and new_c < col_len and image[new_r][new_c] == old_color:
                image[new_r][new_c] = newColor
                dfsColor(new_r, new_c)

        dfsColor(sr, sc)

        return image
