from typing import List


class Solution:
    def singleNonDuplicate(self, nums: List[int]) -> int:
        # hmap = {}
        # for num in nums:
        #     hmap[num] = hmap.get(num, 0) + 1

        # for key in hmap:
        #     if hmap[key] == 1:
        #         return key

        length = len(nums)-1

        def binarySearch(start, end):
            if start > end:
                return start
            mid = (end-start)/2 + start
            if (mid != 0 or nums[mid] != nums[mid-1]) and (mid != length or nums[mid] != nums[mid+1]):
                return nums[mid]
            elif (mid-start+1) % 2 == 0:
                return binarySearch(mid+1, end)
            else:
                return binarySearch(start, mid-1)

        binarySearch(0, length)

        return -1
