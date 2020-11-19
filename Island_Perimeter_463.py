from typing import List


class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        row = len(grid)
        if row == 0:
            return 0
        col = len(grid[0])

        ans = 0
        dirs = [[1, 0], [-1, 0], [0, 1], [0, -1]]

        # count 0's in 4 directions, thats the perimeter of current 1
        for i in range(row):
            for j in range(col):
                if grid[i][j] == 1:
                    for r, c in dirs:
                        new_r = i + r
                        new_c = j + c

                        if new_r < 0 or new_r >= row or new_c < 0 or new_c >= col:
                            ans += 1
                        else:
                            ans += 1 if grid[new_r][new_c] == 0 else 0

        return ans

    def islandPerimeter_using_DP(self, grid: List[List[int]]) -> int:
        row = len(grid)
        if row == 0:
            return 0
        col = len(grid[0])

        dp = [[0 for col_len in range(col)] for row_len in range(row)]
        # print(dp)

        # going top left to bottom right
        for i in range(row):
            for j in range(col):
                total = 0
                if grid[i][j] == 1:
                    if i == 0:
                        total += 1
                    else:
                        total += 1 if grid[i-1][j] == 0 else 0

                    if j == 0:
                        total += 1
                    else:
                        total += 1 if grid[i][j-1] == 0 else 0

                dp[i][j] = total

        # now, going from bottom right to top left, also we keep on ans as the perimeter, so we add it on the go
        ans = 0
        for i in range(row - 1, -1, -1):
            for j in range(col - 1, -1, -1):
                total = dp[i][j]
                if grid[i][j] == 1:
                    if i == row - 1:
                        total += 1
                    else:
                        total += 1 if grid[i+1][j] == 0 else 0

                    if j == col - 1:
                        total += 1
                    else:
                        total += 1 if grid[i][j+1] == 0 else 0

                    dp[i][j] = total
                    ans += total

        return ans


obj = Solution()
print("Test case 1: [[0,1,0,0],[1,1,1,0],[0,1,0,0],[1,1,0,0]], Expected result = 16, Got result =",
      obj.islandPerimeter([[0, 1, 0, 0], [1, 1, 1, 0], [0, 1, 0, 0], [1, 1, 0, 0]]))
print("Test case 2: [[1,1,0],[0,1,1],[1,0,0]], Expected result = 14, Got result =",
      obj.islandPerimeter([[1, 1, 0], [0, 1, 1], [1, 0, 0]]))
print("Test case 3: [[1,1,1]], Expected result = 14, Got result =",
      obj.islandPerimeter([[1, 1, 1]]))
