from typing import List


class Solution:
    def partitionLabels(self, S: str) -> List[int]:
        last_idx = {}

        for i, char in enumerate(S):
            last_idx[char] = i

        result = []
        length = len(S)

        left = 0

        while left < length:
            right = last_idx[S[left]]
            temp_left = left

            while left <= right and right < length:
                right = max(right, last_idx[S[left]])
                left += 1

            number_of_elements = right - temp_left + 1
            result.append(number_of_elements)

        return result


obj = Solution()
print("Expected result = [9,7,8], Got result = ",
      obj.partitionLabels("ababcbacadefegdehijhklij"))
print("Expected result = [6,1,4,8], Got result = ",
      obj.partitionLabels("ababcbfegdehijhklij"))
