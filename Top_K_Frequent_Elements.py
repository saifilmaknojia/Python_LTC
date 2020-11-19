from typing import List
import collections


class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        if k == 0 or len(nums) == 0:
            return []
        count = collections.Counter(nums)
        frequency = list(count.values())
        frequency.sort()

        last_k_list = []
        while frequency and len(last_k_list) < k:
            element = frequency.pop()
            last_k_list.append(element)

        # print(last_k_list)
        result = set()

        for key, val in count.items():
            if val in last_k_list:
                result.add(key)

        return result


obj = Solution()
print("Test case: [1,1,1,2,2,3], K = 2, Expected result = [1,2], Got result =",
      obj.topKFrequent([1, 1, 1, 2, 2, 3], 2))
