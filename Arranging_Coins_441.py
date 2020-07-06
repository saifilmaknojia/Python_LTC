class Solution:
    def arrangeCoins(self, n: int) -> int:
        if n < 2:
            return n
        # binary search
        start = 1
        end = n

        while start < end:
            mid = (end - start) // 2 + start
            sum_of_first_till_mid = (mid * (mid + 1)) // 2

            if sum_of_first_till_mid <= n and sum_of_first_till_mid + mid + 1 > n:
                return mid
            elif sum_of_first_till_mid < n:
                start = mid + 1
            else:
                end = mid - 1

        return start


obj = Solution()
print("Test case: n = 5, Expected result = 2, Got result =", obj.arrangeCoins(5))
print("Test case: n = 8, Expected result = 3, Got result =", obj.arrangeCoins(8))
print("Test case: n = 35, Expected result = 7, Got result =", obj.arrangeCoins(35))
