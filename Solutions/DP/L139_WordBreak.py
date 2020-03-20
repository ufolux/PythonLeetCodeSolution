from typing import List


class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        dic = set()
        max_l = 0
        for c in wordDict:
            dic.add(c)
            max_l = max(max_l, len(c))

        dp = [False] * (len(s) + 1)
        dp[0] = True
        for i in range(1, len(s) + 1):
            for j in range(max(0, i - max_l), i):
                if dp[j] and s[j: i] in dic:
                    dp[i] = True
                    break

        return dp[-1]


s = Solution()
s.wordBreak("leetcode", ["leet", "code"])
