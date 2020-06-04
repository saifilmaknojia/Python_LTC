# from functools import cmp_to_key
from typing import List
import functools


class Solution:
    def twoCitySchedCost(self, costs: List[List[int]]) -> int:
        def numeric_compare(x, y):
            return (x[0] - x[1]) - (y[0] - y[1])

        # costs.sort(key=lambda x: x[0] - x[1])
        costs.sort(key=functools.cmp_to_key((numeric_compare)))
        # costs = sorted(costs, key = functools.cmp_to_key((lambda x, y: -1 if x[0] - x[1] <= y[0] - y[1] else 1)))

        # print(costs)

        length = len(costs)
        min_cost = 0

        for i in range(length//2):
            min_cost += costs[i][0]

        for i in range(length//2, length):
            min_cost += costs[i][1]

        return min_cost


obj = Solution()
print("Expected result = 110, Got result = ", obj.twoCitySchedCost(
    [[10, 20], [30, 200], [400, 50], [30, 20]]))
print("Expected result = 170, Got result = ", obj.twoCitySchedCost(
    [[10, 120], [130, 100], [40, 50], [90, 20]]))
