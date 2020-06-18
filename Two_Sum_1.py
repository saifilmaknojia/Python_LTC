from typing import List


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        mapper = {}
        res = [-1, -1]

        for i, num in enumerate(nums):
            if (target - num) in mapper:
                res[0] = mapper[target - num]
                res[1] = i
                break

            mapper[num] = i

        return res


obj = Solution()
print("Test case: arr = [2, 7, 11, 15], target = 13, Expected result = [0, 2], Got result = ", obj.twoSum(
    [2, 7, 11, 15], 13))
