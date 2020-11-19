from typing import List


class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        result_list = []
        temp_list = []
        length = len(nums)

        def backtrack(idx, temp_list):
            """ Inner method can access variables from outside method, in this case we case make use of nums, length, result_list"""
            if idx > length:
                return

            result_list.append(temp_list.copy())

            for i in range(idx, length):
                temp_list.append(nums[i])
                backtrack(i + 1, temp_list)
                temp_list.pop()

        backtrack(0, temp_list)
        # print(result_list)

        return result_list


obj = Solution()
print("Test case: [1,2,3], Expected result = [[], [1], [1, 2], [1, 2, 3], [1, 3], [2], [2, 3], [3]], Got result =",
      obj.subsets([1, 2, 3]))
