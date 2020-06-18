from typing import List


class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        left = 0
        right = len(numbers)-1

        while left < right:
            curr_sum = numbers[left] + numbers[right]
            if curr_sum == target:
                return [left+1, right+1]
            elif curr_sum > target:
                right -= 1
            else:
                left += 1

        return [-1, -1]


obj = Solution()
print("Test case: array = [2, 7, 11, 15], target = 13, Expected result = [1, 3], Got result = ", obj.twoSum(
    [2, 7, 11, 15], 13))
