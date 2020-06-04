# from functools import cmp_to_key
from typing import List
import functools


class Solution:
    def reorderLogFiles(self, logs: List[str]) -> List[str]:
        def custom_sort(s1, s2):
            idx1 = s1.find(' ')+1
            idx2 = s2.find(' ')+1

            s1_temp = s1[idx1:]
            s2_temp = s2[idx2:]

            if s1_temp[0].isdigit() and s2_temp[0].isdigit():
                return 0
            elif s1_temp[0].isdigit():
                return 1
            elif s2_temp[0].isdigit():
                return -1
            else:
                if s1_temp == s2_temp:
                    return -1 if s1 < s2 else 1
                else:
                    return -1 if s1_temp < s2_temp else 1

        logs.sort(key=functools.cmp_to_key((custom_sort)))

        return logs


obj = Solution()
print('Expected result = ["let1 art can","let3 art zero","let2 own kit dig","dig1 8 1 5 1","dig2 3 6"], Got result = ',
      obj.reorderLogFiles(["dig1 8 1 5 1", "let1 art can", "dig2 3 6", "let2 own kit dig", "let3 art zero"]))

print('Expected result = ["a2 act car","g1 act car","a8 act zoo","ab1 off key dog","a1 9 2 3 1","zo4 4 7"], Got result = ',
      obj.reorderLogFiles(["a1 9 2 3 1", "g1 act car", "zo4 4 7", "ab1 off key dog", "a8 act zoo", "a2 act car"]))
