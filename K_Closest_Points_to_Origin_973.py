from typing import List


class Solution:
    def kClosest(self, points: List[List[int]], K: int) -> List[List[int]]:
        distances = []
        distance_mapper = {}

        def calculateDistance(x, y):
            return x**2 + y**2

        for i, point in enumerate(points):
            gotDistance = calculateDistance(point[0], point[1])
            distances.append(gotDistance)
            distance_mapper[i] = gotDistance

        distances.sort()
        required_distance = distances[K-1]

        result = []

        for i in distance_mapper:
            if distance_mapper.get(i) <= required_distance:
                result.append(points[i])

        return result
