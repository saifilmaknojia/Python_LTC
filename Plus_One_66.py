from typing import List


class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        number = 0
        for digit in digits:
            number = number * 10 + digit

        number += 1

        return [int(x) for x in str(number)]


obj = Solution()
print("Test case: [1, 2, 3], Expected result = [1, 2, 4], Got result = ",
      obj.plusOne([1, 2, 3]))
print("Test case: [9, 9, 9], Expected result = [1, 0, 0, 0], Got result = ",
      obj.plusOne([9, 9, 9]))
