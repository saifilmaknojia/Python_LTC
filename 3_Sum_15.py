from typing import List


class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        # sort and two pointer

        nums.sort()
        result = []
        length = len(nums) - 1
        for i, num in enumerate(nums):
            # if current number is same as previous, we continue because we would already have considered it previously
            if i > 0 and num == nums[i-1]:
                continue

            complement = -num
            left = i + 1
            right = length

            while left < right:
                total = nums[left] + nums[right]

                if total == complement:
                    result.append([num, nums[left], nums[right]])
                    left += 1
                    right -= 1

                    while left < right and nums[left] == nums[left - 1]:
                        left += 1

                    while left < right and nums[right] == nums[right + 1]:
                        right -= 1

                elif total < complement:
                    left += 1
                else:
                    right -= 1

        return result


obj = Solution()
print("Test case: [-1,0,1,2,-1,-4], Expected result = [[-1,-1,2],[-1,0,1]], Got result =",
      obj.threeSum([-1, 0, 1, 2, -1, -4]))
print("Test case: [-1,0,1,2,-1,-4,-3,1,2,-5], Expected result = [[-4, 2, 2], [-3, 1, 2], [-1, -1, 2], [-1, 0, 1]], Got result =",
      obj.threeSum([-1, 0, 1, 2, -1, -4, -3, 1, 2, -5]))
