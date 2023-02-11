# O(N K log K), because it does a sort of O(K log K) where K is max string length for all N strings
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        groups = {}
        for word in strs:
            key = "".join(sorted(word))
            groups.setdefault(key, []).append(word)
        return list(groups.values())

# O(NK) because creating the count tuple is O(K) for each of the N strings
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        groups = {}
        for word in strs:
            key = [0 for i in range(26)]
            for char in word:
                key[ord(char) - ord('a')] += 1
            groups.setdefault(tuple(key), []).append(word)
        return list(groups.values())
