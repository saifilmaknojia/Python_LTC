from typing import List


class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        self.result_list = []

        self.backtrack("", 0, 0, n)

        return self.result_list

    def backtrack(self, st, open_bracket, close_bracket, n):
        # print(st)

        if len(st) == 2*n:
            self.result_list.append(st)
            return

        if open_bracket < n:
            self.backtrack(st + '(', open_bracket + 1, close_bracket, n)

        if close_bracket < open_bracket:
            self.backtrack(st + ')', open_bracket, close_bracket + 1, n)


obj = Solution()
print(
    'Test case: n = 3, Expected result = ["((()))","(()())","(())()","()(())","()()()"], Got result =', obj.generateParenthesis(3))
