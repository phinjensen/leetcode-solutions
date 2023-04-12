# Way harder than it looks! I think there are probably faster/more elegant ways to implement the DSU
# (e.g. the official leetcode editorial uses integers for representative indices), but this works,
# generally. Might be worth trying a DFS version too at some point.
class Solution:
    def accountsMerge(self, accounts: List[List[str]]) -> List[List[str]]:
        self.parents = {}
        self.size = {}
        seen = set()
        names = {}
        for account in accounts:
            names[account[1]] = account[0]
            if account[1] not in seen:
                self.makeSet(account[1])
                seen.add(account[1])
            for email in account[2:]:
                if email not in seen:
                    self.makeSet(email)
                    seen.add(email)
                self.unionSets(account[1], email)
        result = {}
        for account in accounts:
            for email in account[1:]:
                result.setdefault(self.findSet(account[1]), set()).add(email)
        return [[names[head], *sorted(emails)] for head, emails in result.items()]
    
    def makeSet(self, account):
        self.parents[account] = account
        self.size[account] = 1
    
    def findSet(self, account):
        parent = self.parents.get(account)
        if account == parent:
            return account
        self.parents[account] = self.findSet(parent)
        return self.parents[account]
    
    def unionSets(self, a, b):
        a = self.findSet(a)
        b = self.findSet(b)
        if a != b:
            if self.size[a] < self.size[b]:
                a, b = b, a
            self.parents[b] = a
            self.size[a] += self.size[b]
