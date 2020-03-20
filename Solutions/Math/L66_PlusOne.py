from typing import List


class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        for i in range(len(digits) - 1, -1, -1):
            if digits[i] != 9:
                digits[i] = digits[i] + 1
                return digits
            digits[i] = (digits[i] + 1) % 10

        res = [0] * (len(digits) + 1)
        res[0] = 1
        return res


s = Solution()
s.plusOne([9, 9, 9])
