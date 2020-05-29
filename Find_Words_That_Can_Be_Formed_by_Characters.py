from typing import List


class Solution:
    def countCharacters(self, words: List[str], chars: str) -> int:
        res = 0
        arr = [0] * 26

        check = [0] * 26
        for c in chars:
            arr[ord(c)-ord('a')] += 1

        check = arr.copy()
        tick = False
        # print(check)
        for w in words:
            for c in w:
                check[ord(c)-ord('a')] -= 1
                if check[ord(c)-ord('a')] < 0:
                    tick = True
                    break
            if tick == False:
                res = res + len(w)
            check = arr.copy()
            tick = False
        return res

    def input(self):
        print(self.countCharacters(["cat", "bt", "hat", "tree"], "atach"))


obj = Solution()
obj.input()
# print(obj.countCharacters(["cat", "bt", "hat", "tree"], "atach"))
