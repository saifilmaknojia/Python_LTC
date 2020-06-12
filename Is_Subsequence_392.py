class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        s_len = len(s)

        s_idx = 0

        for t_char in t:
            if s_idx == s_len:
                return 1

            if s[s_idx] == t_char:
                s_idx += 1

        return s_idx == s_len


obj = Solution()
print("Test case: s=abc, t=ahbgdc, Expected result=True, Got result= ",
      obj.isSubsequence('abc', 'ahbgdc'))
print("Test case: s=axc, t=ahbgdc, Expected result=False, Got result= ",
      obj.isSubsequence('axc', 'ahbgdc'))
