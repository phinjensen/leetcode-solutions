# Not too bad DFS problem. The trick that got me stuck for a bit was that it's really an undirected graph, but I was treating the adjacency list as a directed graph.

class Solution:
    def makeConnected(self, n: int, connections: List[List[int]]) -> int:
        if len(connections) < n - 1:
            return -1
        
        self.visited = set()
        self.adjacency = {}
        for src, dest in connections:
            self.adjacency.setdefault(src, []).append(dest)
            self.adjacency.setdefault(dest, []).append(src)

        islands = 0
        for i in range(n):
            if i not in self.visited:
                self.dfs(i)
                islands += 1
        
        return islands - 1


    def dfs(self, i):
        self.visited.add(i)
        neighbors = self.adjacency.get(i, [])
        for neighbor in neighbors:
            if neighbor not in self.visited:
                self.dfs(neighbor)
