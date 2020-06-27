import math


class Solution:
    def checkPerfectNumber(self, num: int) -> bool:
        if num <= 1:
            return False
        end = (int)(math.sqrt(num)) + 1
        # starting with total 1, since num will always be divisible by 1
        total = 1
        for i in range(2, end):
            if num % i == 0:
                total += i
                total += num / i
        # print(total)

        return num == total


obj = Solution()
print("Test case: n = 35, Expected result = False, Got result =",
      obj.checkPerfectNumber(35))
print("Test case: n = 28, Expected result = True, Got result =",
      obj.checkPerfectNumber(28))
