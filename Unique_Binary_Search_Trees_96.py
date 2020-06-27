class Solution:
    def numTrees(self, n: int) -> int:
        if n <= 1:
            return 1

        dp = [0] * (n + 1)
        dp[0] = 1

        for i in range(1, n+1):
            for consider_center in range(1, i+1):
                trees_on_left = dp[consider_center - 1]
                trees_on_right = dp[i - consider_center]

                combinations_possible = trees_on_left * trees_on_right
                dp[i] += combinations_possible

        return dp[-1]


obj = Solution()
print("Test case 1: n = 3, Expected result = 5, Got result =", obj.numTrees(3))
print("Test case 2: n = 5, Expected result = 42, Got result =", obj.numTrees(5))
print("Test case 3: n = 8, Expected result = 1430, Got result =", obj.numTrees(8))
