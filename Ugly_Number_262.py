class Solution:
    def isUgly(self, num: int) -> bool:
        if num == 0:
            return False

        div = [2, 3, 5]

        for i in div:
            while num % i == 0:
                num = num / i

            if num == 1:
                return True

        return False


obj = Solution()
print("Test case: num = 8, Expected result = True, Got result =", obj.isUgly(8))
print("Test case: num = 14, Expected result = False, Got result =", obj.isUgly(14))
