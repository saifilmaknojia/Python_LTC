from typing import List


class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        row_len = len(coins) + 1
        col_len = amount + 1

        dp = [[0 for col in range(col_len)] for row in range(row_len)]

        # for col in range(0, col_len):
        #     dp[0][col] = 1

        for row in range(row_len):
            dp[row][0] = 1

        # print(dp)
        for i in range(1, row_len):
            for j in range(1, col_len):
                curr_coin = coins[i-1]
                if j >= curr_coin:
                    dp[i][j] = dp[i-1][j] + dp[i][j - curr_coin]
                else:
                    dp[i][j] = dp[i-1][j]
                # print(i, j, "-->",dp[i][j])

        return dp[-1][-1]


obj = Solution()
print("Test case: 5, [1, 2, 5], Expected result = 3, Got result = ", obj.change(
    4, [1, 2, 5]))
print("Test case: 14, [1,2,5,7,8], Expected result = 28, Got result = ", obj.change(
    14, [1, 2, 5, 7, 8]))
