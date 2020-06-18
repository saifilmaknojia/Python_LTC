class Solution:
    def longestPalindrome(self, s: str) -> str:
        # using expand around center method
        self.max_len = -1
        self.l = 0
        self.r = 0

        length = len(s)
        if length < 2:
            return s

        s_arr = list(s)

        for i in range(length):
            # odd length expansion
            self.expandAroundCenter(i, i, s_arr, length)

            # even length expansion
            self.expandAroundCenter(i, i+1, s_arr, length)

        # print(l, r)
        return s[self.l: self.r+1]

    def expandAroundCenter(self, left, right, arr, length):
        while left >= 0 and right < length and arr[left] == arr[right]:
            if right - left >= self.max_len:
                self.max_len = right - left + 1
                self.l = left
                self.r = right

            left -= 1
            right += 1


obj = Solution()
print("Test case: missisipi, Expected result = issi, Got result =",
      obj.longestPalindrome("missisipi"))
print("Test case: babad, Expected result = bab, Got result =",
      obj.longestPalindrome("babad"))
