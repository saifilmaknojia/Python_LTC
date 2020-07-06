class Solution:
    def hammingDistance(self, x: int, y: int) -> int:
        count = 0
        while x or y:
            if (x ^ y) & 1 == 1:
                count += 1
            x >>= 1
            y >>= 1

        return count


obj = Solution()
print("Test case: x = 3, y = 7, Expected result = 1, Got result =",
      obj.hammingDistance(3, 7))
print("Test case: x = 13, y = 27, Expected result = 3, Got result =",
      obj.hammingDistance(13, 27))
