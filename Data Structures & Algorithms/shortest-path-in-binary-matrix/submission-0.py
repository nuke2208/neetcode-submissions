from collections import deque
class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        q = deque()
        visited = set()
        steps = 1
        n = len(grid)
        if grid[0][0] == 1:
            return -1
        q.append((0,0))
        visited.add((0,0))
        while q:
            for _ in range(len(q)):
                r,c = q.popleft()
                if r == n - 1 and c == n-1:
                    return steps
                for dr, dc in [(0,1),(1,0),(0,-1),(-1,0),(1,1),(1,-1),(-1,1),(-1,-1)]:
                    nr = r + dr
                    nc = c + dc
                    if 0 <= nr < n and 0 <= nc < n and grid[nr][nc] == 0 and (nr,nc) not in visited:
                         q.append((nr,nc))
                         visited.add((nr,nc))
                
                   
            steps = steps + 1
        return -1
        