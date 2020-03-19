class Solution:
    def longestPalindrome(self, s: str) -> int:
        d = {}
        for c in s:
            if c not in d:
                d[c] = 1
            else:
                d[c] = d[c] + 1
        res = 0
        for _, n in d.items():
            res += n - (n & 1)

        return res + 1 if res < len(s) else res


s = Solution()
s.longestPalindrome("ccd")
