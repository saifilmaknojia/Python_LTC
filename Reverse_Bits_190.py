class Solution:
    def reverseBits(self, n: int) -> int:
        ans = 0
        bits = 32
        while bits > 0:
            right_most_bit = n & 1
            ans <<= 1
            ans = ans | right_most_bit
            # print(ans);
            n >>= 1
            bits -= 1

        return ans


obj = Solution()
print("Test case: 00000010100101000001111010011100, Expected result = 00111001011110000010100101000000, Got result =",
      obj.reverseBits(43261596))
