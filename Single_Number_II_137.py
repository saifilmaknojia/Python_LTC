from typing import List


class Solution:
    # bit manipulation solution
    def singleNumber(self, nums: List[int]) -> int:
        foundOnce, foundTwice = 0, 0
        for num in nums:
            foundOnce = ~foundTwice & (num ^ foundOnce)
            foundTwice = ~foundOnce & (num ^ foundTwice)

        return foundOnce


obj = Solution()
print("Test case = [2,3,2,2], Expected result = 3, Got result =",
      obj.singleNumber([2, 3, 2, 2]))
print("Test case = [0,1,0,99,1,0,1], Expected result = 99, Got result =",
      obj.singleNumber([0, 1, 0, 99, 1, 0, 1]))
