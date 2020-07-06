class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        dp = [[0 for col in range(n)] for row in range(m)]

        # first row all entries are 1 because there is only 1 way, i.e - from left
        for i in range(n):
            dp[0][i] = 1
        # similarly, first column all entries are 1 because there is only 1 way, i.e - from top
        for j in range(m):
            dp[j][0] = 1

        # main dp, relation = dp[i][j] = dp[i-1][j] + dp[i][j-1], i.e = sum of left and top
        for i in range(1, m):
            for j in range(1, n):
                dp[i][j] = dp[i-1][j] + dp[i][j-1]

        return dp[-1][-1]


obj = Solution()
print("Test case: m = 4, n = 7, Expected result = 84, Got result =",
      obj.uniquePaths(4, 7))
print("Test case: m = 3, n = 7, Expected result = 28, Got result =",
      obj.uniquePaths(3, 7))
