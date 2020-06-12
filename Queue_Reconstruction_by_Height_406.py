from typing import List
import functools


class Solution:
    def reconstructQueue(self, people: List[List[int]]) -> List[List[int]]:
        def custom_sort(p1, p2):
            if p1[0] != p2[0]:
                return p2[0] - p1[0]
            else:
                return p1[1] - p2[1]

        people.sort(key=functools.cmp_to_key((custom_sort)))

        final_ans = []

        for ppl in people:
            final_ans.insert(ppl[1], ppl)

        return final_ans


obj = Solution()
print("Test case: [[7,0], [4,4], [7,1], [5,0], [6,1], [5,2]], Expected Result = [[5,0], [7,0], [5,2], [6,1], [4,4], [7,1]], Got result = ",
      obj.reconstructQueue([[7, 0], [4, 4], [7, 1], [5, 0], [6, 1], [5, 2]]))
