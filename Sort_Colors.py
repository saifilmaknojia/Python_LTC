from typing import List


class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """

        red = 0
        white = 0
        blue = len(nums)-1

        while white <= blue:
            if nums[white] == 2:
                nums[white], nums[blue] = nums[blue], nums[white]
                blue -= 1
            elif nums[white] == 0:
                nums[white], nums[red] = nums[red], nums[white]
                red += 1
                white += 1
            else:
                white += 1

        print("Got result =", nums)


obj = Solution()
print("Test case: [2,0,2,1,1,0,1,1,1,2,2,2,0,1,0,0,1,1,2], Expected result = [0,0,0,0,0,1,1,1,1,1,1,1,1,2,2,2,2,2,2]")
obj.sortColors([2, 0, 2, 1, 1, 0, 1, 1, 1, 2, 2, 2, 0, 1, 0, 0, 1, 1, 2])
