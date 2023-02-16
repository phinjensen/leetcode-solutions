# Insert, search, and startswith are all O(n) where n is the length of the word or prefix being inserted or searched.
class Trie:
    def __init__(self):
        self.root = {}

    def insert(self, word: str) -> None:
        node = self.root
        for i, c in enumerate(word):
            node = node.setdefault(c, {})
        node["complete"] = True
        

    def search(self, word: str) -> bool:
        node = self.root
        for c in word:
            if c in node:
                node = node[c]
            else:
                return False
        if "complete" in node:
            return True
        return False
        

    def startsWith(self, prefix: str) -> bool:
        node = self.root
        for c in prefix:
            if c in node:
                node = node[c]
            else:
                return False
        return True


# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)
