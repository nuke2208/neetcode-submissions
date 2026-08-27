class Solution:
    from collections import deque
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        rows = len(grid)
        cols = len(grid[0])
        q = deque()
        for i in range(rows):
            for j in range(cols):
                if grid[i][j] == 0:
                    q.append((i,j))
        while q:
            r, c = q.popleft()
            for dr, dc in [(0,1),(1,0),(-1,0),(0,-1)]:
                nr = r + dr
                nc = c + dc
                if 0 <= nr < rows and 0<=nc<cols and grid[nr][nc] == 2147483647:
                    grid[nr][nc] = grid[r][c] + 1
                    q.append((nr,nc))
        

        