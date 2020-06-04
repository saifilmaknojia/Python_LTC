from typing import List


class Solution:
    def reverseString(self, s: List[str]) -> str:
        """
        Do not return anything, modify s in-place instead.
        """
        length = len(s)-1
        mid = len(s)//2

        for i in range(mid):
            s[i], s[length-i] = s[length-i], s[i]

        return s


obj = Solution()
print('Expected result = ["o","l","l","e","h"], Got result = ',
      obj.reverseString(["h", "e", "l", "l", "o"]))

print('Expected result = ["a","m","a","n","a","P"," ",":","l","a","n","a","c"," ","a"," ",",","n","a","l","p"," ","a"," ",",","n","a","m"," ","A"], Got result = ',
      obj.reverseString(["A", " ", "m", "a", "n", ",", " ", "a", " ", "p", "l", "a", "n", ",", " ", "a", " ", "c", "a", "n", "a", "l", ":", " ", "P", "a", "n", "a", "m", "a"]))
