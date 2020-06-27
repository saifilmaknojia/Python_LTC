from collections import deque
import math


class Solution:
    def numSquares(self, n: int) -> int:
        """ DP AND BFS solution, O(N ^ h/2) time """
        if n <= 3:
            return n
        squares = [i**2 for i in range(0, (int)(math.sqrt(n) + 1))]
        cache = set()
        de_que = deque([])

        de_que.append(n)
        res = 1

        while de_que:
            size = len(de_que)
            for _ in range(0, size):
                polled = de_que.popleft()
                for square in squares:
                    if polled == square:
                        return res
                    if (polled - square) not in cache:
                        cache.add(polled - square)
                        de_que.append(polled - square)
            res += 1

        return res

    def numSquares_onlyDP(self, n: int) -> int:
        """ Only DP solution, performs poorly, O(N root N) time"""
        if n <= 1:
            return n

        squares = [i ** 2 for i in range(0, (int)(math.sqrt(n)) + 1)]
        # print(squares)
        dp = [n] * (n + 1)
        dp[0] = 0

        for num in range(1, n+1):
            for square in squares:
                if square <= num:
                    dp[num] = min(dp[num - square] + 1, dp[num])
            # print("min squares for", num, "is -->", dp[num])
        return dp[-1]


obj = Solution()
print("Test case: n = 35, Expected result = 3, Got result =", obj.numSquares(35))
print("Test case: n = 1421, Expected result = 2, Got result =", obj.numSquares(1421))
