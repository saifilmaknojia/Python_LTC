class Solution:
    def addBinary(self, a: str, b: str) -> str:
        # return bin(int(a, 2) + int(b, 2))[2:]

        a_idx = len(a)-1
        b_idx = len(b)-1

        carry = 0
        result = ""
        while a_idx > -1 or b_idx > -1:
            total = 0
            if a_idx > -1 and a[a_idx] == '1':
                total += 1
            if b_idx > -1 and b[b_idx] == '1':
                total += 1

            total += carry
            # print(total)
            if total >= 2:
                carry = 1
                result += '1' if total % 2 else '0'
            else:
                result += '1' if total else '0'
                carry = 0

            a_idx -= 1
            b_idx -= 1

        if carry:
            result += '1'

        return result[::-1]


obj = Solution()
print("Test case: a = '1010', b = '1011', Expected result = '10101', Got result =",
      obj.addBinary("1010", "1011"))
print("Test case: a = '11', b = '1', Expected result = '100', Got result =",
      obj.addBinary("11", "1"))
