class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        dp = [True if i == 0 else False for i in range(len(s)+1)]
        for i in range(1, len(s)+1):
            for word in wordDict:
                if len(word) <= i:
                    if not dp[i-len(word)]:
                        continue
                    start = i-len(word)
                    if s[start:i] == word:
                        dp[i] = True
                        break
        return dp[-1]
