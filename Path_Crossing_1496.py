class Solution:
    def isPathCrossing(self, path: str) -> bool:
        x, y = 0, 0
        path_cache = set()
        path_cache.add(tuple([0, 0]))

        for direction in path:
            if direction == 'N':
                y += 1
            elif direction == 'S':
                y -= 1
            elif direction == 'E':
                x += 1
            else:
                x -= 1

            new_path = tuple([x, y])

            if new_path in path_cache:
                return True
            else:
                path_cache.add(new_path)

        return False


obj = Solution()
print("Test case: 'NES', Expected result = False, Got result =",
      obj.isPathCrossing("NES"))
print("Test case: 'NESWW', Expected result = True, Got result =",
      obj.isPathCrossing("NESWW"))
