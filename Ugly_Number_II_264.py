class Solution:
    def nthUglyNumber(self, n: int) -> int:
        list_two = [2]
        list_three = [3]
        list_five = [5]

        two_ptr = 0
        three_ptr = 0
        five_ptr = 0

        # since 1 is the first ugly number we start with 1 and reduce n by 1
        res = 1
        n = n - 1

        while n > 0:
            res = min(list_two[two_ptr],
                      list_three[three_ptr], list_five[five_ptr])
            # print(res)
            n -= 1

            list_two.append(2 * res)
            list_three.append(3 * res)
            list_five.append(5 * res)

            if res == list_two[two_ptr]:
                two_ptr += 1
            if res == list_three[three_ptr]:
                three_ptr += 1
            if res == list_five[five_ptr]:
                five_ptr += 1

        return res


obj = Solution()
print("Test case: num = 10, Expected result = 12, Got result =", obj.nthUglyNumber(12))
print("Test case: num = 23, Expected result = 48, Got result =", obj.nthUglyNumber(23))
