from collections import deque

class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        fresh_oranges = 0
        minutes = 0
        queue = deque()
        for r in range(len(grid)):
            for c in range(len(grid[r])):
                if grid[r][c] == 2:
                    queue.append((r, c, minutes))
                elif grid[r][c] == 1:
                    fresh_oranges += 1
        while queue:
            r, c, minutes = queue.pop()
            for rn, cn in (r+1,c), (r-1, c), (r, c+1), (r, c-1):
                if 0 <= rn < len(grid) and 0 <= cn < len(grid[rn]) and grid[rn][cn] == 1:
                    grid[rn][cn] = 2
                    fresh_oranges -= 1
                    queue.appendleft((rn, cn, minutes + 1))
        return -1 if fresh_oranges > 0 else minutes
