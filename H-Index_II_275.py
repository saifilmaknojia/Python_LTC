from typing import List
from bisect import bisect_left


class Solution:
    def hIndex(self, citations: List[int]) -> int:

        length = len(citations)

        if length == 0:
            return 0

        for h_idx in range(length, 0, -1):
            pos = bisect_left(citations, h_idx)
            # print(h_idx, pos)
            number_of_elements_on_right = length - pos
            number_of_element_on_left = pos - 0

            if number_of_elements_on_right >= h_idx and number_of_element_on_left <= length - h_idx:
                return h_idx

        return 0


obj = Solution()
print("Test case 1: [0,1,3,5,6], Expected result = 3, Got result =", obj.hIndex(
    [0, 1, 3, 5, 6]))
print("Test case 2: [0,1,3,5,6,11,35,67], Expected result = 5, Got result =", obj.hIndex(
    [0, 1, 3, 5, 6, 11, 35, 67]))
