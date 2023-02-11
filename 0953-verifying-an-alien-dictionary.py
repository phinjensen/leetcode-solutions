# Time complexity would be O(M * N) where M is the length of the longest word and N is the length of words.
# Space complexity is O(M + A) where A is the length of the alphabet, which is constant in this case, giving us O(M)
class Solution:
    def isSorted(self, prev, word):
        for i in range(len(prev)):
            if i >= len(word):
                return False
            if prev[i] > word[i]:
                return False
            elif prev[i] < word[i]:
                return True
        return True

    def isAlienSorted(self, words: List[str], order: str) -> bool:
        positions = {}
        for i, c in enumerate(order):
            positions[c] = i
        prev = [positions[c] for c in words[0]]
        for word in words[1:]:
            word = [positions[c] for c in word]
            if not self.isSorted(prev, word):
                return False
            prev = word
        return True
