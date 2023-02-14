# I initially wrote this by myself almost perfectly EXCEPT one huge mistake: I marked nodes as visited after popping them off the queue, not before putting them on. That led to way to many double checks of nodes, which made it fail the time limit.
from queue import Queue

class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        islands = 0
        for r in range(len(grid)):
            for c in range(len(grid[r])):
                if grid[r][c] != "1":
                    continue
                islands += 1
                queue = Queue()
                queue.put((r,c))
                while not queue.empty():
                    rc, cc = queue.get()
                    for rn, cn in (rc - 1, cc), (rc + 1, cc), (rc, cc - 1), (rc, cc + 1):
                        if 0 <= rn < len(grid) and 0 <= cn < len(grid[0]) and grid[rn][cn] == "1":
                            grid[rn][cn] = "0"
                            queue.put((rn, cn))
        return islands
