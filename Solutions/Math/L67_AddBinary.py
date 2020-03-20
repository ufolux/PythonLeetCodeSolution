class Solution:
    def addBinary(self, a: str, b: str) -> str:
        i = len(a) - 1
        j = len(b) - 1
        carry = 0
        res = ""
        while i >= 0 or j >= 0:
            da = ord(a[i]) - ord('0') if i >= 0 else 0
            db = ord(b[j]) - ord('0') if j >= 0 else 0
            res += str((da + db + carry) % 2)
            carry = (da + db + carry) >> 1
            i = i - 1
            j = j - 1
        res += str(carry if carry > 0 else "")
        return res[::-1]


s = Solution()
print(s.addBinary("111", "1"))