from typing import List


class Solution:
    def combinationSum4(self, nums: List[int], target: int) -> int:
        # same as coin change 2 problem
        length = len(nums)
        if length == 0:
            return 0

        nums.sort()

        dp = [0] * (target+1)
        dp[0] = 1

        for make_current_sum in range(1, target+1):
            for using_current_num in nums:
                if using_current_num > make_current_sum:
                    break

                dp[make_current_sum] += dp[make_current_sum - using_current_num]

        return dp[-1]


obj = Solution()
print("Test case: nums = [1, 2, 3], target = 5, Expected result = 13, Got result =",
      obj.combinationSum4([1, 2, 3], 5))
print("Test case: nums = [1, 2, 3, 6], target = 11, Expected result = 560, Got result =",
      obj.combinationSum4([1, 2, 3, 6], 11))
