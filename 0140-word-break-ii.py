# Time complexity is something like O(W * L * S) where W is the size of the dictionary, L is the length of the longest word in the dictionary, and S is the length of the input string. It's hard to say...
# Space complexity would be similar, but without the longest word factor: O(W * S).
# This is probably totally wrong.
class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> List[str]:
        self.memo = {}
        self.dict = wordDict
        result = self.helper(s)
        print(self.memo)
        return result
    
    def helper(self, s: str) -> List[str]:
        if self.memo.get(s) != None:
            return self.memo[s]
        
        answers = []
        for word in self.dict:
            if word == s:
                answers.append(word)
            elif s.startswith(word):
                answers.extend([word + " " + answer for answer in self.helper(s[len(word):])])
        self.memo[s] = answers
        return answers
