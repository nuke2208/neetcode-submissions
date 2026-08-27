class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        maxcount = 0
        visited = set()
        n = len(grid)
        m = len(grid[0])
        def dfs(i,j):
            if i <0 or i >= n:
                return 0
            if j<0 or j >= m:
                return 0
            if grid[i][j] == 0:
                return 0
            if (i,j) in visited:
                return 0
            visited.add((i,j))
            count = 1
            count += dfs(i+1,j)
            count += dfs(i-1,j)
            count += dfs(i,j+1)
            count += dfs(i,j-1)
            return count
        for i in range(n):
            for j in range(m):
                count = dfs(i,j)
                if count > maxcount:
                    maxcount = count
        return maxcount
        