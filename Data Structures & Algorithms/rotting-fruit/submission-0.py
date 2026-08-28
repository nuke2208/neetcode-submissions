from collections import deque
class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        m = len(grid)
        n = len(grid[0])
        q = deque()
        fresh = 0
        count = 0
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 2:
                    q.append((i,j))
                if grid[i][j] == 1:
                    fresh = fresh + 1
        while q and fresh > 0:
            for _ in range(len(q)):
                r,c = q.popleft()
                for dr, dc in [(1,0),(0,1),(-1,0),(0,-1)]:
                    nr = r + dr
                    nc = c + dc
                    if 0 <= nr < m and 0 <= nc < n and grid[nr][nc] == 1:
                        grid[nr][nc] = 2
                        q.append((nr,nc))
                        fresh = fresh - 1
            count += 1
        if fresh > 0:
            return -1
        return count
        