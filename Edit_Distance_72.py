class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        len_w1 = len(word1)+1
        len_w2 = len(word2)+1

        dp = [[0 for _ in range(len_w2)] for _ in range(len_w1)]

        # adding indexes to first row
        for col in range(len_w2):
            dp[0][col] = col

        # adding indexes to first column
        for row in range(len_w1):
            dp[row][0] = row

        for i in range(1, len_w1):
            for j in range(1, len_w2):
                if word1[i-1] == word2[j-1]:
                    dp[i][j] = dp[i-1][j-1]
                else:
                    dp[i][j] = 1 + min(dp[i-1][j-1], dp[i-1][j], dp[i][j-1])

        # print(dp)
        return dp[len_w1 - 1][len_w2 - 1]


obj = Solution()
print("Expected result = 27, Got result = ", obj.minDistance(
    "pneumonoultramicroscopicsilicovolcanoconiosis", "ultramicroscopically"))
print("Expected result = 5, Got result = ",
      obj.minDistance("intention", "execution"))
print("Expected result = 3, Got result = ", obj.minDistance("horse", "ros"))
