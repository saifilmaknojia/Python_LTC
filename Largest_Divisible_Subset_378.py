from typing import List


class Solution:
    def largestDivisibleSubset(self, nums: List[int]) -> List[int]:
        # O(N^2) time and space solution

        length = len(nums)
        if length < 2:
            return nums

        nums.sort()

        dp_list = [[] for x in range(length)]
        max_len_subset = 0
        result_list = []

        for i in range(0, length):
            max_idx = -1
            curr_max_subset_length = 0
            for j in range(0, i):
                if nums[i] % nums[j] == 0:
                    if len(dp_list[j]) > curr_max_subset_length:
                        max_idx = j
                        curr_max_subset_length = len(dp_list[j])

            if max_idx != -1:
                dp_list[i] = list(dp_list[max_idx])

            dp_list[i].append(nums[i])

            if len(dp_list[i]) > max_len_subset:
                result_list = dp_list[i]
                max_len_subset = len(dp_list[i])

        return result_list


obj = Solution()

print("Test case 1: [1,2,3], Expected result = [1, 2], Got result =",
      obj.largestDivisibleSubset([1, 2, 3]))
print("Test case 2: [1,2,3,4,5,6,7,8,9,10,11,12,13], Expected result = [1,2,4,8], Got result =",
      obj.largestDivisibleSubset([[1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]]))
print("Test case 3: [4,8,10,240], Expected result = [4,8,240], Got result =",
      obj.largestDivisibleSubset([4, 8, 10, 240]))
