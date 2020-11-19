from typing import List
from collections import defaultdict
from collections import deque


class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        # first those courses who do not have any incoming edges
        # will need incoming_degree_tracker, graph for outgoing edges
        # from.add(to), incoming_degree_tracker[to]++
        # reduce degree_tracker in the loop when it comes to zero, add it to the queue for processing and add it to the result list

        graph = defaultdict(list)
        # [[] for i in range(numCourses)]
        incoming_degree_tracker = [0] * numCourses
        result = []

        for to, fromm in prerequisites:
            graph[fromm].append(to)
            incoming_degree_tracker[to] += 1

        queue = deque([])

        for i, degree in enumerate(incoming_degree_tracker):
            if degree == 0:
                queue.append(i)
                result.append(i)

        while queue:
            size = len(queue)
            for i in range(size):
                curr = queue.popleft()

                for child in graph[curr]:
                    incoming_degree_tracker[child] -= 1
                    if incoming_degree_tracker[child] == 0:
                        queue.append(child)
                        result.append(child)

        return result if len(result) == numCourses else []


obj = Solution()
print("Test case: numcourses = 4, prerequisites = [[1,0],[2,0],[3,1],[3,2]], Expected result = [0, 1, 2, 3] or [0, 2, 1, 3], Got result =", obj.findOrder(
    4, [[1, 0], [2, 0], [3, 1], [3, 2]]))
