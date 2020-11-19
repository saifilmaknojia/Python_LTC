class Solution:
    def reverseWords(self, s: str) -> str:
        words_arr = s.split()
        words_arr.reverse()
        ans = " ".join(words_arr)

        return ans


obj = Solution()
print("Test case 1: 'the sky is blue', Expected result = 'blue is sky the', Got result =",
      obj.reverseWords('the sky is blue'))
print("Test case 2: 'a good   example', Expected result = 'example good a', Got result =",
      obj.reverseWords('a good   example'))
print("Test case 3: '  hello world!  ', Expected result = 'world! hello', Got result =",
      obj.reverseWords('  hello world!  '))
