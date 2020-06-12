import bisect
from typing import List


class Solution:
    def suggestedProducts(self, products: List[str], searchWord: str) -> List[List[str]]:
        products.sort()
        length = len(products)
        result = []

        word = ""
        for s in searchWord:
            word += s
            idx = bisect.bisect_left(products, word)

            max_forward = min(idx + 3, length)

            temp_list = []
            for i in range(idx, max_forward):
                if products[i].startswith(word):
                    temp_list.append(products[i])
                else:
                    break

            result.append(temp_list)

        return result


obj = Solution()
print('Test case: Products = ["bags","baggage","banner","box","cloths"], searchWord = "bat", Expected result = [["baggage","bags","banner"],["baggage","bags","banner"],[]], Got result = ',
      obj.suggestedProducts(["bags", "baggage", "banner", "box", "cloths"], "bat"))
