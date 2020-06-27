from typing import List


class Solution:
    def sumZero(self, n: int) -> List[int]:
        end = n // 2
        start = -1 * end
        ans = [x for x in range(start, end+1) if x != 0]

        if n % 2:
            ans.append(0)

        return ans
