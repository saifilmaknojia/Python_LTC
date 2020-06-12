from typing import List
import math


class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        row_len = len(coins) + 1
        col_len = amount + 1

        dp = [[0 for col in range(col_len)] for row in range(row_len)]

        for col in range(1, col_len):
            dp[0][col] = math.inf

        # for row in range(row_len):
        #     dp[row][0] = math.inf

        # print(dp)

        for i in range(1, row_len):
            for j in range(1, col_len):
                curr_coin = coins[i-1]
                if j >= curr_coin:
                    dp[i][j] = min(1 + dp[i][j-curr_coin], dp[i-1][j])
                else:
                    dp[i][j] = dp[i-1][j]

        return -1 if dp[-1][-1] == math.inf else dp[-1][-1]


obj = Solution()
print("Test case = [1,2,5,6,7,8,9,10], 145, Expected result = 15, Got result =",
      obj.coinChange([1, 2, 5, 6, 7, 8, 9, 10], 145))
