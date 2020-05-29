from typing import List


class Solution:
    # same as - 1143. Longest Common Subsequence
    def maxUncrossedLines(self, A: List[int], B: List[int]) -> int:
        a_len = len(A)+1
        b_len = len(B)+1

        if a_len == 0 or b_len == 0:
            return 0
# O(N square) time and space
        dp = [[0 for col in range(b_len)] for row in range(a_len)]

        # print(dp)

        for i in range(1, a_len):
            for j in range(1, b_len):
                # if the number in A at ith position and the number in B at jth position match
                # then we take the diagonal entry and add 1 to it
                if A[i-1] == B[j-1]:
                    dp[i][j] = 1 + dp[i-1][j-1]
                else:  # else we take the max from the top row or the left column, i.e whichever gives us the max either A or B
                    dp[i][j] = max(dp[i-1][j], dp[i][j-1])

        return dp[a_len-1][b_len-1]


obj = Solution()
print("Expected ans = 2", "Got result = ",
      obj.maxUncrossedLines([1, 4, 2], [1, 2, 4]))
print("Expected ans = 3", "Got result = ", obj.maxUncrossedLines(
    [2, 5, 1, 2, 5], [10, 5, 2, 1, 5, 2]))
print("Expected ans = 2", "Got result = ",
      obj.maxUncrossedLines([1, 3, 7, 1, 7, 5], [1, 9, 2, 5, 1]))
