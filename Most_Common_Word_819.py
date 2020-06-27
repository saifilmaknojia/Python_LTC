import collections
from typing import List


class Solution:
    def mostCommonWord(self, paragraph: str, banned: List[str]) -> str:
        ban_set = set(banned)

        punctuations = "?!.,';'"

        # replace punctuation with space
        for ch in punctuations:
            paragraph = paragraph.replace(ch, ' ')

        count = collections.Counter(word for word in paragraph.lower().split())

        # print(count)

        max_len = 0
        result_word = ""

        for word, ct in count.items():
            # print(word, ct)
            if word not in ban_set and ct > max_len:
                result_word = word
                max_len = ct

        return result_word


obj = Solution()
print("Test case: paragraph = 'Bob hit a ball, the hit BALL flew far after it was hit.', banned = ['hit'], Expected result = ball, Got result =", obj.mostCommonWord(
    'Bob hit a ball, the hit BALL flew far after it was hit.', ['hit']))
