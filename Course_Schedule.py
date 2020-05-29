from typing import List
from collections import deque


class Solution:
    hasCycle = False

    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        # DFS version
        graph = [[] for _ in range(numCourses)]

        for post, pre in prerequisites:
            graph[pre].append(post)

        onStack = [False] * numCourses
        visited = [False] * numCourses

        for i in range(numCourses):
            if visited[i] == False and len(graph[i]) > 0:
                self.performDFS(onStack, visited, graph, i)

            if self.hasCycle == True:
                return False

        return True

    def performDFS(self, onStack, visited, graph, idx):
        if self.hasCycle:  # if cycle is already found, then we dont need to perform any further recursions
            return

        if onStack[idx] == True:  # if OnStack[idx] is true then it means we are trying to do recursion on the idx which is already on stack, so there is a cycle
            self.hasCycle = True
            return

        onStack[idx] = True
        for child in graph[idx]:
            if visited[child] == False:
                self.performDFS(onStack, visited, graph, child)

        onStack[idx] = False
        visited[idx] = True
        return

    ############################################################################################################

    def canFinish_BFS(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        # BFS version
        in_degree = [0] * numCourses
        graph = [[] for _ in range(numCourses)]

        # for i in range(numCourses):
        #     graph.append([])

        for post, pre in prerequisites:
            graph[pre].append(post)
            in_degree[post] += 1

        # print(graph)

        queue = deque([])
        count = 0
        for i in range(numCourses):
            if in_degree[i] == 0:
                queue.append(i)
                count += 1

        while len(queue) > 0:
            curr = queue.popleft()
            for child in graph[curr]:
                in_degree[child] -= 1

                if in_degree[child] == 0:
                    queue.append(child)
                    count += 1

        return count == numCourses
