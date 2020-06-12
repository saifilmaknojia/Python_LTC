from bisect import bisect_left
import random
from typing import List


class Solution:

    def __init__(self, w: List[int]):
        length = len(w)
        self.probabilities = [0] * length

        total_weight = sum(w)
        running_probability = 0.0

        for i, weight in enumerate(w):
            probability = weight / total_weight

            running_probability += probability

            self.probabilities[i] = running_probability

        # print(self.probabilities)

    def pickIndex(self) -> int:
        rand_number_between_0_and_1 = random.random()
        binary_search_result = bisect_left(
            self.probabilities, rand_number_between_0_and_1)
        # print(binary_search_result, " --> ", rand_number_between_0_and_1)
        return binary_search_result


# Your Solution object will be instantiated and called as such:
obj = Solution([5, 10, 15, 5])

print("Result = ")

# calling pickIndex 10 times
for i in range(10):
    print(obj.pickIndex(), end=" ")
