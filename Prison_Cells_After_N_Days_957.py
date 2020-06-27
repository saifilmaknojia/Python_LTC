from typing import List


class Solution:
    def prisonAfterNDays(self, cells: List[int], N: int) -> List[int]:
        result_list = []
        cache = set()
        string_version = "".join(str(x) for x in cells)
        temp = N
        while temp > 0:
            next_ = [0] * 8

            for i in range(1, 7):
                if (cells[i-1] and cells[i+1]) or (not cells[i-1] and not cells[i+1]):
                    next_[i] = 1
                else:
                    next_[i] = 0

            cells = next_
            string_version = "".join(str(x) for x in cells)

            if string_version not in cache:
                cache.add(string_version)
                result_list.append(next_)
            else:
                break
            temp -= 1

        if temp == 0:
            return cells

        length = len(result_list)

        while N > length:
            N %= length

        return result_list[N-1]


obj = Solution()
print("Test case: [0,1,0,1,1,0,0,1], N = 73, Expected result = [0,1,1,0,0,1,0,0], Got result = ",
      obj.prisonAfterNDays([0, 1, 0, 1, 1, 0, 0, 1], 73))

print("Test case: [0,1,0,1,1,0,0,1], N = 7, Expected result = [0,0,1,1,0,0,0,0], Got result = ",
      obj.prisonAfterNDays([0, 1, 0, 1, 1, 0, 0, 1], 7))
